from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters import Text
from etc.keyboards import Keyboards
from services.goodsService import GoodsService
from services.oneService import OneService
from services.orderService import OrderService
from services.textService import Texts
from services.userService import UserService
from loader import dp


@dp.callback_query_handler(lambda call: call.data.startswith('see_order:'))
async def order_info(call: CallbackQuery):
    order_id = call.data.split(':')[1]
    order = OrderService.Get(order_id)

    order_text = f"Заказ №{order.id}\n" \
                 f"Дата заказа: {order.date}\n" \
                 f"Сумма: {order.total}\n" \
                 f"Статус: {order.status}\n"

    # Отправка сообщения с информацией о заказе и кнопками "Назад" и "Повторить заказ"
    await call.message.answer(order_text, reply_markup=Keyboards.OrderInfo(order))
    
@dp.callback_query_handler(lambda c: c.data.startswith("repeat_order:"), state="*")
async def repeat_order(c: CallbackQuery, state: FSMContext):
    if state:
        await state.finish()
    user_id = c.from_user.id
    user = UserService.Get(user_id)

    order_id = int(c.data.split(":")[1])
    order = OrderService.Get(order_id)
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


@dp.callback_query_handler(lambda call: call.data.startswith('profile:orders_history'))
async def order_info(c: CallbackQuery):
    user_id = c.from_user.id
    user = UserService.Get(user_id)
    orders = OrderService.GetOrdersByUserId(user_id)
    if not orders:
        await c.answer(Texts.YourOrdersHistoryIsEmpty, show_alert=True)
        return
    await c.message.answer(Texts.YourOrderHistory, reply_markup=Keyboards.OrderHistory(orders))
    

@dp.message_handler(Text(Texts.Profile), state="*")
async def show_personal_cabinet(m: Message, state: FSMContext):
    if state:
        await state.finish()
    user_id = m.from_user.id
    user = UserService.Get(user_id)
    orders = OrderService.GetOrdersByUserId(user_id)
    text = f"Личный кабинет пользователя {user.fullname}\n"
    if user.is_authenticated:
        text += "\n<b>✅ Вход выполнен ✅</b>\n"
    await m.answer(text=text, reply_markup=Keyboards.Profile(orders))