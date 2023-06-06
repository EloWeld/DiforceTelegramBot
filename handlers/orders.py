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
from utils import cutText, format_phone_number, getCartPrice, prepareCartItemToSend, prepareGoodItemToSend


async def get_order_text(state: FSMContext = None, user=None):
    if user and state:
        stateData = await state.get_data()
        p = stateData.get('pay_method', None)
        d = stateData.get('deliv_method', None)

        address = next((x["Name"] for x in user["addresses"] if x["ID"]
                        == stateData.get("deliv_address_id", None)), None)
        address_text = f'Адрес доставки: <b>{address}</b>\n' if d == 'delivery' and address else ''
        cart_price = getCartPrice(user)
        order_cost_text = f"{cart_price:,}₽".replace(',', ' ')
        if d == 'delivery' and cart_price < 3000:
            order_cost_text += " + 200₽ доставка".replace(',', ' ')

        text = f"\n\nМетод оплаты: <b>{verbose[p]}</b>\n"\
            f"Метод доставки: <b>{verbose[d]}</b>\n"\
            f"{address_text}" \
            f"Сумма к оплате: <b>{order_cost_text}</b>"
    else:
        text = ""
    return "✅ Все товары из корзины есть на складе в достаточном количестве. Укажите метод оплаты и доставки и подтвердите создание заказа" + text


@dp.message_handler(state="AddDeliveryAddress")
async def _(m: Message, state: FSMContext):
    if len(m.text) > 1000:
        await m.answer("❌ Слишком длинный адрес!")
        return
    user = UserService.Get(m)
    addr_id = str(uuid4())[:10]
    user['addresses'].append(dict(
        Name=m.text,
        ID=addr_id
    ))
    UserService.Update(user)
    await state.update_data(deliv_address_id=addr_id)
    stateData = await state.get_data()
    await m.answer("Укажите адрес доставки",
                   reply_markup=Keyboards.DelivAddress(user,
                                                       stateData.get(
                                                           'deliv_method', None),
                                                       stateData.get(
                                                           'deliv_address_id', None)
                                                       ))


@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE), text_contains="|OrderActions:", state="*")
async def cart_callback_handler(c: CallbackQuery, state: FSMContext):
    """Handle order-related callback queries."""
    action = c.data.split(":")[1]
    user = UserService.Get(c)

    if action == "confirm_order":
        stateData = await state.get_data()
        p = stateData.get('pay_method', None)
        d = stateData.get('deliv_method', None)

        await c.message.edit_text(text=await get_order_text(state, user),
                                  reply_markup=Keyboards.ConfirmOrder(p, d))

    if action == "choose_pay_method":
        await c.answer()
        method = c.data.split(":")[2]
        await state.update_data(pay_method=method)
        stateData = await state.get_data()
        p = stateData.get('pay_method', None)
        d = stateData.get('deliv_method', None)

        await c.message.edit_text(text=await get_order_text(state, user),
                                  reply_markup=Keyboards.ConfirmOrder(p, d))
    if action == "choose_address":
        await c.answer()
        stateData = await state.get_data()
        if 'deliv_address_id' in stateData:
            await state.set_data({x: y for x, y in stateData.items() if x != 'deliv_address_id'})
            address_id = -1
        else:
            address_id = c.data.split(":")[2]
            await state.update_data(deliv_address_id=address_id)
        is_delivery = stateData.get('deliv_method', None) == "delivery"
        await c.message.edit_text("Укажите адрес доставки", reply_markup=Keyboards.DelivAddress(user, is_delivery, address_id))

    if action == "choose_deliv_method":
        method = c.data.split(":")[2]
        stateData = await state.get_data()
        if method == "delivery":
            await c.answer()
            is_delivery = stateData.get('deliv_method', None) == 'delivery'
            deliv_address_id = stateData.get('deliv_address_id', None)
            await c.message.edit_text("Укажите адрес доставки", reply_markup=Keyboards.DelivAddress(user, is_delivery, deliv_address_id))
            return
        if method == "delivery_true":
            deliv_address_id = stateData.get('deliv_address_id', None)
            if deliv_address_id == None:
                await c.answer("！ Выберите адрес ！", show_alert=True)
                return
            method = method.replace("_true", '')
            if 'deliv_method' in stateData and stateData['deliv_method'] == 'delivery':
                await state.update_data(deliv_method=None)
                is_delivery = False
            else:
                is_delivery = True
                await state.update_data(deliv_method='delivery')
            await c.answer()
            await c.message.edit_text("Укажите адрес доставки", reply_markup=Keyboards.DelivAddress(user, is_delivery, deliv_address_id))
            return
        await c.answer()
        await state.update_data(deliv_method=method)
        stateData = await state.get_data()
        p = stateData.get('pay_method', None)
        d = stateData.get('deliv_method', None)

        await c.message.edit_text(text=await get_order_text(state, user),
                                  reply_markup=Keyboards.ConfirmOrder(p, d))

    if action == "add_deliv_address":
        await c.message.edit_text("🚛 Укажите адрес доставки\n\nПример: 141007, Красноярск, улица Горького, 14",
                                  reply_markup=Keyboards.back("|OrderActions:choose_deliv_method:delivery"))
        await state.set_state("AddDeliveryAddress")

    if action == "make_an_order_store":
        storeID = "000000001"
        stateData = await state.get_data()
        pay_method = stateData.get('pay_method')
        deliv_method = stateData.get('deliv_method')
        deliv_address_id = stateData.get('deliv_address_id')

        if pay_method is None:
            await c.answer("☑️ Укажите метод оплаты", show_alert=True)
            return

        if deliv_method is None:
            await c.answer("☑️ Укажите метод доставки", show_alert=True)
            return

        if not user.is_authenticated:
            await c.message.answer(f"⚠️ Заказ доступен только авторизированным пользователям! Для авторизации нажмите кнопку <b>{Texts.AuthButton}</b>")
            return

        cart = user.get('cart', {})
        for product_id, cartItem in cart.items():
            good = MDB.Goods.find_one({'ProductID': product_id})
            cartItem['Price'] = GoodsService.GetTargetPrice(
                user, good) if good else -1

        try:
            success_order_data = OneService.CreateOrder(user, storeID)
        except Exception as e:
            loguru.logger.error(
                f"Error on create order {e}: {traceback.format_exc()}")
            await c.message.answer("❌ не удалось создать заказ в 1С!")
            return

        if success_order_data:
            cart_price = getCartPrice(user)
            saved_card = cart.copy()
            order_data = OrderService.CreateWithBot(success_order_data, user)
            order_data['DeliveryMethod'] = deliv_method
            order_data['PayMethod'] = pay_method
            order_data['DeliveryAddress'] = deliv_address_id
            order_data['DeliveryPrice'] = 200 if cart_price < 3000 and order_data['DeliveryMethod'] == 'delivery' else 0
            order_data['CartPrice'] = cart_price

            if order_data['DeliveryAddress']:
                for addr in user['addresses']:
                    if addr['ID'] == order_data['DeliveryAddress']:
                        order_data['DeliveryAddress'] = addr['Name']

            MDB.Orders.insert_one(order_data)

            if user['cart'] == {}:
                await c.answer("😶 Корзина пуста!", show_alert=True)

            # Уменьшаем количество на складах купленных товаров
            # Сейчас не нужно
            # for cartItemID in user['cart']:
            #     MDB.Goods.update_one(dict(ProductID=cartItemID), {"$inc": {"QtyInStore": -1 * user['cart'][cartItemID]['Quantity']}})

            user['cart'] = {}
            UserService.Update(user)
            await c.message.answer(f"✅ Заказ <code>#{success_order_data['CreatedOrderID']}</code> оформлен!")
            await c.message.delete()

            try:
                order_text = f"📦 Номер заказа: <code>{success_order_data['CreatedOrderID']}</code>\n\n"
                order_text += "📋 Состав заказа:\n"

                for product_id, cartItem in saved_card.items():
                    price = cartItem['Price']
                    quantity = cartItem['Quantity']
                    item_total = price * quantity

                    order_text += f"<code>{quantity} шт</code> * <code>{price}₽</code> = <code>{item_total}₽</code> | <code>{product_id}</code> | <b>{cartItem['ProductName']}</b>\n\n"
                order_cost_text = f"{cart_price:,}₽".replace(',', ' ')
                if order_data['DeliveryMethod'] == 'delivery' and cart_price < 3000:
                    order_cost_text += f" + {order_data['DeliveryPrice']:,}₽ доставка".replace(',', ' ')
                formatted_summary = f"Общая сумма: <code>{order_cost_text}</code>"
                order_text += formatted_summary
                order_text += f"\n\n🚩 Адрес доставки: <code>{order_data.get('DeliveryAddress', 'Не указан')}</code>\n"
                order_text += f"🚩 Способ доставки: <code>{verbose[order_data['DeliveryMethod']]}</code>\n"
                order_text += f"🚩 Способ оплаты: <code>{verbose[order_data['PayMethod']]}</code>\n"

                user_info_text = f"👤 ФИО: <code>{user['diforce_data']['FullName']}</code>\n"
                user_info_text += f"📧📞 Email/Тел.: <code>{user['diforce_data'].get('Email', '/').replace('<', '').replace('>', '')}</code>/<code>{format_phone_number(user['diforce_data'].get('Phone', ''))}</code>\n"
                user_info_text += f"🏷️💲 Тип цен: <code>{user['diforce_data']['ContractType']}</code>\n"

                order_manager_message = f"⭐ Пользователь <a href='tg://user?id={user.id}'>{user.fullname}</a> (@{user.username}) Сделал заказ!\n\n" + \
                    user_info_text + order_text
                await bot.send_message(Consts.OrderManagerID, order_manager_message, reply_markup=types.ReplyKeyboardRemove())
            except Exception as e:
                loguru.logger.error(
                    f"Can't send message to user about order: {e}, {traceback.format_exc()}")
        else:
            await c.message.answer("❌ Не удалось создать заказ в 1С!")

    if action == "make_an_order":
        await c.answer()

        if not user.is_authenticated:
            await c.message.answer(f"⚠️ Заказ доступен только авторизированным пользователям! Для авторизации нажмите кнопку <b>{Texts.AuthButton}</b>")
            return

        goods = []
        cartItems = user['cart']
        for key, cartItem in cartItems.items():
            good = MDB.Goods.find_one(dict(ProductID=cartItem['ProductID']))

            if good:
                try:
                    good['QtyInStore'] = [x for x in good['QuantityInStores']
                                          if x['store_id'] == "000000001"][0]['quantity']
                except Exception:
                    good['QtyInStore'] = 0
                cartItem['Price'] = GoodsService.GetTargetPrice(user, good)
                goods.append(good)

            cartItem['good_item'] = good if good is not None else dict(
                QtyInStore=0)

        can_order = True
        for key, cItem in cartItems.items():
            if cItem['Quantity'] > cItem['good_item']['QtyInStore']:
                can_order = False
                if cItem['good_item']['QtyInStore'] == 0:
                    await c.message.answer(f"⚠️ Товара <b>{cutText(cItem['ProductName'], 50)}</b> на складе вообще не осталось, измените корзину")
                else:
                    await c.message.answer(f"⚠️ Товара <b>{cutText(cItem['ProductName'], 50)}</b> на складе осталось только <b>{cItem['good_item']['QtyInStore']}</b> шт., а у вас в корзине <b>{cItem['Quantity']}</b> шт., измените корзину")

        if can_order:
            await c.message.edit_text(await get_order_text(state, user), reply_markup=Keyboards.ConfirmOrder())
