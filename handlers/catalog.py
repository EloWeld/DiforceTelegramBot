from etc.filters import AntiSpam
from etc.keyboards import Keyboards
from etc.m_user import User
from etc.v83_controller import V83Controller
from loader import dp

from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text,ChatTypeFilter
from aiogram.types import Message, ChatType, BotCommand


@dp.message_handler(Text("Товары"), AntiSpam(), ChatTypeFilter(ChatType.PRIVATE), state="*")
async def _(m: Message, state: FSMContext):
    if state:
        await state.finish()

    goods = V83Controller.getAllGoods()

    await m.answer(f"Список товаров({len(goods)}):\n")
    for g_index in range(0, len(goods), 5):
        await m.answer('\n'.join([x['Name'] for x in goods[g_index:g_index+5]]))
