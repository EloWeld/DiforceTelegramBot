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
from utils import cutText, format_phone_number, prepareCartItemToSend, prepareGoodItemToSend


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

    messageText = prepareGoodItemToSend(good, cartItem, user)
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

async def increment_cart_item_count(c, user, goodsID, good, cartItem):
    user.cart[goodsID]['Quantity'] += 1
    UserService.Update(user)

    messageText = prepareCartItemToSend(good, cartItem)

    if c.message.caption:
        await c.message.edit_caption(messageText, reply_markup=c.message.reply_markup)
    else:
        await c.message.edit_text(messageText, reply_markup=c.message.reply_markup)

async def send_cart_item(c, user, goodsID, good, cartItem):
    await c.answer()
    await sendCartItem(good, cartItem, user)

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
            cartItems[-1]['ProductName'] = cutText(
                cartItems[-1]['ProductName'], 35)
            cart_price += x * cartItems[-1].Quantity

    cartText = '\n'.join(Texts.CartItemTextFormat.format(**x)
                         for x in cartItems)

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
    action = c.data.split(":")[1]
    user = UserService.Get(c)

    if action == "hide":
        await c.message.delete()
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

    actions = {
        "dec_count": decrement_cart_item_count,
        "remove_from_cart": remove_from_cart,
        "inc_count": increment_cart_item_count,
        "see_cart_item": send_cart_item
    }

    if action in actions:
        goodsID = c.data.split(':')[2]
        cartItem = user.cart[goodsID]
        good = GoodsService.GetGoodByID(goodsID)
        await actions[action](c, user, goodsID, good, cartItem)