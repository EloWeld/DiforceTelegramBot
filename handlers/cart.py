import asyncio
import base64
from copy import copy
import datetime
import traceback
from uuid import uuid4
from dotdict import dotdict

import loguru
from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text, ChatTypeFilter
from aiogram.types import Message, ChatType, BotCommand, CallbackQuery, ContentType

from etc.filters import AntiSpam
from etc.keyboards import Keyboards
from loader import MDB, dp, bot, Consts
from services.goodsService import GoodsService
from services.oneService import OneService
from services.orderService import OrderService
from services.textService import Texts
from services.userService import UserService
from utils import cutText, prepareCartItemToSend, prepareGoodItemToSend


async def sendCartItem(good, cartItem, user):
    """Send cart item message with or without image."""
    messageText = prepareCartItemToSend(good, cartItem)
    keyboard = Keyboards.cartItem(good)

    if 'ProductImage' in good and good['ProductImage']:
        await bot.send_photo(user.id, base64.b64decode(good['ProductImage']), caption=messageText, reply_markup=keyboard)
    else:
        await bot.send_message(user.id, messageText, reply_markup=keyboard)


async def showCart(user):
    """Show cart with all items."""
    cartItems = []
    cart_price = 0

    if user['cart'] == {}:
        await bot.send_message(user.id, Texts.YourCartIsEmpty)
        return
    for cartItemID in user['cart']:
        cartItems += [dotdict(user['cart'][cartItemID])]
        good = MDB.Goods.find_one(dict(ProductID=cartItems[-1].ProductID))
        x = GoodsService.GetTargetPrice(user, good)
        if not x:
            cartItems = cartItems[:-1]
            continue
        else:
            cartItems[-1]['OneQtyPrice'] = x
            cartItems[-1]['SummaryPrice'] = x * cartItems[-1].Quantity
            cartItems[-1]['ProductName'] = cutText(cartItems[-1]['ProductName'], 35)
            cart_price += x * cartItems[-1].Quantity

    cartText = '\n'.join(Texts.CartItemTextFormat.format(**x) for x in cartItems)

    cartPriceString = f"{cart_price:,}".replace(',', ' ')

    await bot.send_message(user.id, Texts.YourCartMessage.format(cart_text=cartText,
                                                                 cart_price=cartPriceString), reply_markup=Keyboards.yourCart(cartItems))


@dp.message_handler(Text(Texts.CartButton), AntiSpam(), ChatTypeFilter(ChatType.PRIVATE), state="*")
async def show_cart_handler(m: Message, state: FSMContext):
    """Handle 'show cart' request."""
    if state:
        await state.finish()
    user = UserService.Get(m)

    await showCart(user)


@dp.message_handler(state="cart_product_quantity")
async def set_cart_product_quantity(m: Message, state: FSMContext):
    """Handle setting cart product quantity."""
    stateData = await state.get_data()

    if m.text.isdigit() and int(m.text) > 0:
        quantity = int(m.text)
    else:
        await m.answer(Texts.IncorrectQuantity)
        return

    user = UserService.Get(m.from_user.id)
    cartItem = None
    for x in user.cart:
        if x == stateData['cartItemID']:
            user.cart[x]['Quantity'] = quantity
            cartItem = user.cart[x]
            break
    good = GoodsService.GetGoodByID(cartItem['ProductID'], False)
    if good['QtyInStore'] == 0:
        await m.answer(f"❌ {quantity} единиц товара нет на складе, количество не изменено")
        return
    
    UserService.Update(user)
    if stateData['from_adding']:
        await m.answer(f"✅ Количество изменено на <code>{quantity}шт</code>!", reply_markup=Keyboards.startMenu(user))
    else:
        await sendCartItem(good, cartItem, user)
    
    if state:
        await state.finish()


@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE), text_contains="|Cart:", state="*")
async def cart_callback_handler(c: CallbackQuery, state: FSMContext):
    """Handle cart-related callback queries."""
    if state:
        await state.finish()
    action = c.data.split(":")[1]
    user = UserService.Get(c)

    if action == "hide":
        await c.message.delete()
    if action == "clear_all":
        user['cart'] = {}
        UserService.Update(user)
        await c.message.answer("✅ Корзина очищена")
        await c.message.delete()
        
    if action == "make_an_order_store":
        storeID = "000000001"
        await c.answer()

        if not user.is_authenticated:
            await c.message.answer(f"⚠️ Заказ доступен только авторизированным пользователям! Для авторизации нажмите кнопку <b>{Texts.AuthButton}</b>")
            return

        cart = user.get('cart', {})
        for product_id, cartItem in cart.items():
            good = MDB.Goods.find_one({'ProductID': product_id})
            if good:
                cartItem['Price'] = GoodsService.GetTargetPrice(user, good)
            else:
                cartItem['Price'] = -1

        success_order_data = OneService.CreateOrder(user, storeID)

        if success_order_data:
            saved_card = cart.copy()
            order_data = OrderService.CreateWithBot(success_order_data, user)
            MDB.Orders.insert_one(order_data)
            user['cart'] = {}
            UserService.Update(user)
            
            await c.message.answer("✅ Заказ сделан!")

            try:
                full_cart_summary = 0
                order_text = f"Номер заказа: <code>{success_order_data['CreatedOrderID']}</code>\n\n"
                order_text += "Состав заказа:\n"
                
                for product_id, cartItem in saved_card.items():
                    price = cartItem['Price']
                    quantity = cartItem['Quantity']
                    item_total = price * quantity
                    full_cart_summary += item_total
                    
                    order_text += f"<code>{quantity} шт</code> * <code>{price}₽</code> = <code>{item_total}₽</code> | <code>{product_id}</code> | <b>{cartItem['ProductName']}</b>\n\n"
                
                formatted_summary = f"Общая стоимость корзины: <code>{full_cart_summary:,}₽</code>".replace(',', ' ')
                order_text += formatted_summary
                
                order_manager_message = f"⭐ Пользователь <a href='tg://user?id={user.id}'>{user.fullname}</a> (@{user.username}) Сделал заказ!\n\n" + order_text
                await bot.send_message(Consts.OrderManagerID, order_manager_message)
            except Exception as e:
                loguru.logger.error(f"Can't send message to user about order: {e}, {traceback.format_exc()}")
        else:
            await c.message.answer("❌ Не удалось создать заказ!")
    if action == "make_an_order(old)":
        goods = []
        for cartItem in list(user['cart'].values()):
            good = MDB.Goods.find_one(dict(ProductID=cartItem['ProductID']))
            try:
                good['QtyInStore'] = [x for x in good['QuantityInStores'] if x['store_id'] == "000000001"][0]['quantity']
            except Exception:
                good['QtyInStore'] = 0
                
            if good:
                cartItem['Price'] = GoodsService.GetTargetPrice(user, good)
                goods.append(good)
        
        # Проверить наличие каджой вещи на складах
        t = "❕ Проверьте наличие на складах и выберите откуда закажите товар\n\n"
        all_stores = {}
        realy_stores = {}

        
        # Собираем список всех уникальных идентификаторов складов
        unique_store_ids = ["000000001"]

        for good in goods:
            qty = [x for x in list(user['cart'].values()) if x['ProductID'] == good['ProductID']][0]['Quantity']
            t += f"💠 [{qty}шт.] <b>{cutText(good['ProductName'], 50)}</b>:\n"
            
            for store_id in unique_store_ids:
                store = next((s for s in good['QuantityInStores'] if s['store_id'] == store_id), None)
                
                if store is not None:
                    all_stores[store_id] = store
                else:
                    store = {"quantity": 0}
                
                if store_id not in realy_stores:
                    realy_stores[store_id] = True
                
                # Check if other goods are available in the necessary quantity in the current store
                other_goods_available = all(
                    next((s['quantity'] for s in other_good['QuantityInStores'] if s['store_id'] == store_id), 0) >= [x for x in list(user['cart'].values()) if x['ProductID'] == other_good['ProductID']][0]['Quantity']
                    for other_good in goods if other_good['ProductID'] != good['ProductID']
                )

                if store['quantity'] < qty:
                    realy_stores[store_id] = False
                    symbol = "⛔"
                elif other_goods_available:
                    symbol = "✅"
                else:
                    symbol = "⚠️"
                if 'store_name' in store:
                    t += f"    {symbol} [{store['quantity']} шт.] <b>{store['store_name']}</b>\n"

        realy_stores = {k: v for k, v in all_stores.items() if realy_stores[k]}

        t += "\n\n"
        if '⛔' in t:
            t += "⛔ — товара в таком количестве нет на складе\n\n"
        if '⚠️' in t:
            t += "⚠️ — такой товар есть в указаном количестве на складе, но остальные товары в необходимом количестве есть только на других складах\n\n"
        if '✅' not in t:
            t += "🤷‍♂️ Вы не можете оформить заказ так как нет подходящих складов под вашу корзину"
        await c.message.edit_text(t, reply_markup=Keyboards.ChooseStore(realy_stores))
        
        
    if action == "make_an_order":
        await c.answer()
        
        if not user.is_authenticated:
            await c.message.answer(f"⚠️ Заказ доступен только авторизированным пользователям! Для авторизации нажмите кнопку <b>{Texts.AuthButton}</b>")
            return
        
        goods = []
        cartItems = user['cart']
        for key, cartItem in cartItems.items():
            good = MDB.Goods.find_one(dict(ProductID=cartItem['ProductID']))
            try:
                good['QtyInStore'] = [x for x in good['QuantityInStores'] if x['store_id'] == "000000001"][0]['quantity']
            except Exception:
                good['QtyInStore'] = 0
                
            if good:
                cartItem['Price'] = GoodsService.GetTargetPrice(user, good)
                goods.append(good)
                
            cartItem['good_item'] = good if good else None

        can_order = True
        for key, cItem in cartItems.items():
            if cItem['Quantity'] > cItem['good_item']['QtyInStore']:
                can_order = False
                if cItem['good_item']['QtyInStore'] == 0:
                    await c.message.answer(f"⚠️ Товара <b>{cutText(cItem['ProductName'], 50)}</b> на складе вообще не осталось, измените корзину")
                else:
                    await c.message.answer(f"⚠️ Товара <b>{cutText(cItem['ProductName'], 50)}</b> на складе осталось только <b>{cItem['good_item']['QtyInStore']}</b> шт., а у вас в корзине <b>{cItem['Quantity']}</b> шт., измените корзину")
            
                
        if can_order:
            await c.message.edit_text("✅ Все товары из корзины есть на складе в достаточном количестве, подтвердите создание заказа", reply_markup=Keyboards.ConfirmOrder())
       
    if action == "back":
        await showCart(user)
        await c.message.delete()
    if action == "cancel_scq":
        await state.finish()
        await c.message.delete()
    if action == "specify_cart_quantity":
        cartItemID = c.data.split(":")[2]
        await c.message.answer(Texts.SpecifyCartQuantity, reply_markup=Keyboards.CancelCartQuantity())
        await state.set_state("cart_product_quantity")
        await state.update_data(cartItemID=cartItemID, from_adding=False)
    if action == "specify_cart_quantity_2":
        cartItemID = c.data.split(":")[2]
        await c.message.edit_text(Texts.SpecifyCartQuantity, reply_markup=Keyboards.CancelCartQuantity())
        await state.set_state("cart_product_quantity")
        await state.update_data(cartItemID=cartItemID, from_adding=True)

    if action in ['dec_count', 'inc_count', 'see_cart_item', 'remove_from_cart']:
        goodsID = c.data.split(':')[2]
        cartItem = user.cart[goodsID]
        good = GoodsService.GetGoodByID(goodsID)

        if action == "dec_count":
            if user.cart[goodsID]['Quantity'] == 1:
                await c.answer(Texts.ClickRemovePopup.format(btn=Texts.RemoveButton), show_alert=True)
                return

            user.cart[goodsID]['Quantity'] -= 1
            UserService.Update(user)

            messageText = prepareGoodItemToSend(good, cartItem)
            if c.message.caption:
                await c.message.edit_caption(messageText, reply_markup=c.message.reply_markup)
            else:
                await c.message.edit_text(messageText, reply_markup=c.message.reply_markup)
        if action == "remove_from_cart":
            del user.cart[goodsID]
            UserService.Update(user)

            await c.message.answer(Texts.CartItemRemoved)
            await c.message.delete()
            await asyncio.sleep(0.3)
            await showCart()
        if action == "inc_count":
            user.cart[goodsID]['Quantity'] += 1
            UserService.Update(user)

            messageText = prepareCartItemToSend(good, cartItem)

            if c.message.caption:
                await c.message.edit_caption(messageText, reply_markup=c.message.reply_markup)
            else:
                await c.message.edit_text(messageText, reply_markup=c.message.reply_markup)
        if action == "see_cart_item":
            await c.answer()
            await sendCartItem(good, cartItem, user)