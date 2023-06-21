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
from services.textService import Texts, verbose
from services.userService import UserService
from utils import cutText, format_phone_number, format_plural, getCartPrice, prepareCartItemToSend, prepareGoodItemToSend, tryDelete


async def sendCartItem(good, cartItem, user):
    """Send cart item message with or without image."""
    messageText = prepareCartItemToSend(good, cartItem, user)
    keyboard = Keyboards.cartItem(good)

    if 'ProductImage' in good and good['ProductImage']:
        await bot.send_photo(user.id, base64.b64decode(good['ProductImage']), caption=messageText, reply_markup=keyboard)
    else:
        await bot.send_message(user.id, messageText, reply_markup=keyboard)


async def decrement_cart_item_count(c, user, goodsID, good, cartItem):
    if user.cart[goodsID]['Quantity'] == 1:
        await c.answer(Texts.ClickRemovePopup.format(btn=Texts.RemoveButton), show_alert=True)
        return

    user.cart[goodsID]['Quantity'] -= 1
    UserService.Update(user)

    messageText = prepareCartItemToSend(good, cartItem, user)
    
    if c.message.caption:
        await c.message.edit_caption(messageText, reply_markup=c.message.reply_markup)
    else:
        await c.message.edit_text(messageText, reply_markup=c.message.reply_markup)

async def remove_from_cart(c, user, goodsID, good, cartItem):
    del user.cart[goodsID]
    UserService.Update(user)

    await c.message.answer(Texts.CartItemRemoved)
    await c.message.delete()
    await asyncio.sleep(0.3)
    await showCart()
    
async def remove_from_cart_2(c: CallbackQuery, user, goodsID, good, cartItem):
    del user.cart[goodsID]
    UserService.Update(user)

    await c.answer(Texts.CartItemRemoved)
    text = prepareGoodItemToSend(good, user)
    await c.message.edit_text(text, reply_markup=Keyboards.goodOptions(user, good, c.data.split(":")[-1]))

async def increment_cart_item_count(c, user, goodsID, good, cartItem):
    if good['QtyInStore'] < user.cart[goodsID]['Quantity'] + 1:
        await c.answer("❌ Товара в таком количестве на складе нет", show_alert=True)
        return
    user.cart[goodsID]['Quantity'] += 1
    UserService.Update(user)

    messageText = prepareCartItemToSend(good, cartItem, user)

    if c.message.caption:
        await c.message.edit_caption(messageText, reply_markup=c.message.reply_markup)
    else:
        await c.message.edit_text(messageText, reply_markup=c.message.reply_markup)

async def send_cart_item(c, user, goodsID, good, cartItem):
    await c.answer()
    await sendCartItem(good, cartItem, user)


async def showCart(user, start: int=0):
    """Show cart with all items."""
    cartItems = []

    if user['cart'] == {}:
        await bot.send_message(user.id, Texts.YourCartIsEmpty)
        return
    
    for cartItemID, cartItem in list(user['cart'].items())[start:start+30]:
        cartItems.append(dotdict(cartItem))
        good = MDB.Goods.find_one(dict(ProductID=cartItems[-1].ProductID))
        x = GoodsService.GetTargetPrice(user, good)
        if not x:
            cartItems = cartItems[:-1]
            continue
        else:
            cartItems[-1]['OneQtyPrice'] = x
            cartItems[-1]['SummaryPrice'] = x * cartItems[-1].Quantity
            cartItems[-1]['ProductName'] = cutText(
                cartItems[-1]['ProductName'], 35)

    cartText = '\n'.join(Texts.CartItemTextFormat.format(**x)
                         for x in cartItems)
    
    if len(user['cart']) - 30 > 0:
        cartText += f"\n И ещё {format_plural(len(user['cart']) - 30, 'товар', 'товара', 'товаров')}"

    cartPriceString = f"{getCartPrice(user):,}".replace(',', ' ')

    await bot.send_message(user.id, Texts.YourCartMessage.format(cart_text=cartText,
                                                                 cart_price=cartPriceString), reply_markup=Keyboards.yourCart(cartItems, start))



@dp.message_handler(state="cart_product_quantity")
async def set_cart_product_quantity(m: Message, state: FSMContext):
    """Handle setting cart product quantity."""
    stateData = await state.get_data()

    if m.text.isdigit() and int(m.text) > 0:
        quantity = int(m.text)
    else:
        ans = await m.answer(Texts.IncorrectQuantity)
        await asyncio.sleep(3)
        await tryDelete(m)
        await tryDelete(ans)
        
        return

    user = UserService.Get(m.from_user.id)
    cartItem = None
    good = GoodsService.GetGoodByID(stateData['cartItemID'], False)
    
    if quantity > good['QtyInStore']:
        ans = await m.answer(f"❌ {quantity} единиц товара нет на складе, максимальное количество - <code>{good['QtyInStore']}</code>. Количество не изменено, введите ещё раз")
        await asyncio.sleep(3)
        await tryDelete(m)
        await tryDelete(ans)
        return
    
    for x in user.cart:
        if x == stateData['cartItemID']:
            user.cart[x]['Quantity'] = quantity
            cartItem = user.cart[x]
            break
        
    if good['QtyInStore'] == 0:
        ans = await m.answer(f"❌ {quantity} единиц товара нет на складе, количество не изменено")
        await asyncio.sleep(3)
        await tryDelete(m)
        await tryDelete(ans)
        return

    UserService.Update(user)
    if stateData['from_adding']:
        ans = await m.answer(f"✅ Количество изменено на <code>{quantity}шт</code>!", reply_markup=Keyboards.startMenu(user))
        if 'msg_from_good_msg' in stateData:
            text = prepareCartItemToSend(good, cartItem, user)
            await stateData['msg_from_good_msg'].edit_text(text, reply_markup=stateData['msg_from_good_msg'].reply_markup)
            await state.set_state(stateData['last_state'])
        await asyncio.sleep(3)
        await tryDelete(m)
        await tryDelete(ans)
    else:
        await sendCartItem(good, cartItem, user)



@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE), text_contains="|Cart:", state="*")
async def cart_callback_handler(c: CallbackQuery, state: FSMContext):
    """Handle cart-related callback queries."""
    action = c.data.split(":")[1]
    user = UserService.Get(c)

    if action == "hide":
        await c.message.delete()

    if action == "main":
        start = 0
        if len(c.data.split(":")) == 2:
            start = int(c.data.split(":")[2])
        if start < 0:
            await c.answer("Вы в начале")
            return
        elif start > len(user['cart']):
            await c.answer("Вы в конце")
            return
        await showCart(user, start=start)
    if action == "clear_all":
        user['cart'] = {}
        UserService.Update(user)
        await c.message.answer("✅ Корзина очищена")
        await c.message.delete()
    if action == "back":
        await showCart(user)
        await c.message.delete()
    if action == "cancel_scq":
        await state.finish()
        await c.message.delete()
    if action == "cancel_scq_2":
        stateData = await state.get_data()
        text = prepareCartItemToSend(MDB.Goods.find_one(dict(ProductID= stateData['cartItemID'])), [user['cart'][x] for x in user['cart'] if x == stateData['cartItemID']][0], user)
        await c.message.edit_text(text, reply_markup=stateData['saved_reply_markup'])
    if action == "specify_cart_quantity":
        cartItemID = c.data.split(":")[2]
        await c.message.answer(Texts.SpecifyCartQuantity, reply_markup=Keyboards.CancelCartQuantity())
        await state.set_state("cart_product_quantity")
        await state.update_data(cartItemID=cartItemID, from_adding=False)
    if action == "specify_cart_quantity_2":
        cartItemID = c.data.split(":")[2]
        await state.update_data(saved_reply_markup=c.message.reply_markup, last_state=await state.get_state())
        await c.message.edit_text(Texts.SpecifyCartQuantity, reply_markup=Keyboards.CancelCartQuantity2())
        await state.set_state("cart_product_quantity")
        await state.update_data(cartItemID=cartItemID, from_adding=True, msg_from_good_msg=c.message)

    actions = {
        "dec_count": decrement_cart_item_count,
        "remove_from_cart": remove_from_cart,
        "remove_from_cart_2": remove_from_cart_2,
        "inc_count": increment_cart_item_count,
        "see_cart_item": send_cart_item
    }

    if action in actions:
        goodsID = c.data.split(':')[2]
        cartItem = user.cart[goodsID]
        good = GoodsService.GetGoodByID(goodsID)
        await actions[action](c, user, goodsID, good, cartItem)