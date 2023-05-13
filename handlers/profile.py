import datetime
import traceback
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters import Text
import loguru
from etc.helpers import rdotdict
from etc.keyboards import Keyboards
from services.goodsService import GoodsService
from services.oneService import OneService
from services.orderService import OrderService
from services.textService import Texts
from services.userService import UserService
from loader import dp
from utils import cutText


@dp.callback_query_handler(lambda call: call.data.startswith('see_order:'))
async def order_info(call: CallbackQuery):
    order_id = call.data.split(':')[1]
    user_id = call.data.split(':')[2]
    order = OrderService.Get(order_id, user_id)
    order_items_text = '\n'.join(f"[{product['qty']} шт.] * <a href='https://t.me/DiforceBot?start=good_{product['id']}'>{cutText(product['name'], 30):30}</a> = <code>{product['summary']:,}₽</code>" for product in order['items'])
    order_text = f"""Заказ №<code>{order.id}</code>\n
Дата заказа: <code>{order.created_at.strftime('%Y-%m-%d %H:%M:%S')}</code>

{"🤖 Заказ через бота" if order.created_with_bot else "🌐 Заказ через сайт"}

Сумма заказа: <code>{order['amount']:,}₽</code>
Состав заказа:
{
    order_items_text
}
"""f"" 

    # Отправка сообщения с информацией о заказе и кнопками "Назад" и "Повторить заказ"
    await call.message.edit_text(order_text, reply_markup=Keyboards.OrderInfo(order))
    
@dp.callback_query_handler(lambda c: c.data.startswith("repeat_order:"), state="*")
async def repeat_order(c: CallbackQuery, state: FSMContext):
    if state:
        await state.finish()
    user_id = c.from_user.id
    user = UserService.Get(user_id)

    order_id = int(c.data.split(":")[1])
    order = OrderService.Get(order_id, user.diforce_data.ID)
    order_items = order.items
    # Здесь проверяйте наличие товаров на складе и выводите соответствующие уведомления
    await check_order_availability_and_show_warnings(order_items, user_id)
    # Затем предоставьте возможность пользователю редактировать заказ, если это необходимо
    await edit_order(order_id, user_id)


def check_availability(item):
    good = GoodsService.GetGoodByID(item['id'])
    quantity_in_stores = sum([x['quantity'] for x in good['QuantityInStores']])
    return quantity_in_stores > 0


def check_order_availability_and_show_warnings(order):
    warnings = []
    for item in order.items:
        # Замените эту строку на проверку доступности товара item в вашей базе данных
        availability = check_availability(item)
        if not availability:
            warnings.append(f"Товар {item['name']} недоступен.")
    return warnings

async def edit_order(order_id, user_id):
    # Здесь реализуйте логику редактирования заказа, позволяя пользователю изменять количество товаров или добавлять/удалять позиции
    pass


@dp.callback_query_handler(lambda call: call.data.startswith('profile'))
async def order_info(c: CallbackQuery):
    options = c.data.split(':')
    if len(options) == 1:
        # Profile
        user_id = c.from_user.id
        user = UserService.Get(user_id)
        text = f"Личный кабинет пользователя {user.fullname}\n"
        if user.is_authenticated:
            text += "\n<b>✅ Вход выполнен ✅</b>\n"
        await c.message.edit_text(text=text, reply_markup=Keyboards.Profile(user))
    elif options[1] == "orders_history":
        user_id = c.from_user.id
        user = UserService.Get(user_id)
        
        if not user['diforce_data']:
            await c.answer(Texts.YouAreLoggedOut, show_alert=True)
            return
        
        d_orders = OrderService.GetOrdersByUser(user)
        
            
        if not d_orders:
            await c.answer(Texts.YourOrdersHistoryIsEmpty, show_alert=True)
            return
        await c.message.edit_text(Texts.YourOrderHistory, reply_markup=Keyboards.OrderHistory(d_orders, user.diforce_data.ID))
        
    elif options[1] == "logout_popup":
        await c.message.answer(Texts.LogoutPopupText, reply_markup=Keyboards.Popup("profile:logout"))        
        await c.answer()
    elif options[1] == "logout":
        user_id = c.from_user.id
        user = UserService.Get(user_id)
        user['is_authenticated'] = False
        user['diforce_data'] = None
        UserService.Update(user)
        await c.message.answer(Texts.YouLoggedOut, reply_markup=Keyboards.startMenu(user))
        await c.message.delete()
    

@dp.message_handler(Text(Texts.Profile), state="*")
async def show_personal_cabinet(m: Message, state: FSMContext):
    if state:
        await state.finish()
    user_id = m.from_user.id
    user = UserService.Get(user_id)
    text = f"Личный кабинет пользователя {user.fullname}\n"
    if user.is_authenticated:
        text += "\n<b>✅ Вход выполнен ✅</b>\n"
    await m.answer(text=text, reply_markup=Keyboards.Profile(user))
