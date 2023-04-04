import asyncio
import base64
from dotdict import dotdict

import loguru
from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text, ChatTypeFilter
from aiogram.types import Message, ChatType, BotCommand, CallbackQuery, ContentType

from etc.filters import AntiSpam
from etc.keyboards import Keyboards
from loader import dp, bot, Consts
from services.goodsService import GoodsService
from services.oneService import OneService
from services.textService import Texts
from services.userService import UserService


def prepareCartItemToSend(good, cartItem):
    """Prepare cart item message text for sending."""
    good['Price'] = f"{good['Price']:,}".replace(',', ' ')
    messageText = Texts.GoodCard.format(
        **good) + Texts.CartItemMessage.format(**cartItem)
    return messageText


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
        good = GoodsService.GetGoodByID(cartItems[-1].ProductID)
        cart_price += GoodsService.GetTargetPrice(user, good) * cartItems[-1].Quantity

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
    
    UserService.Update(user)
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
    if action == "make_an_order":
        await c.message.answer("Заказ сделан")
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
        await state.update_data(cartItemID=cartItemID)

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

            messageText = prepareCartItemToSend(good, cartItem)
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
            await sendCartItem(good, cartItem)