from etc.filters import AntiSpam
from etc.keyboards import Keyboards
from etc.m_user import User
from loader import dp

from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ChatType, BotCommand


@dp.message_handler(Command("/"), AntiSpam(), state="*")
async def _(m: Message, command: Command.CommandObj, state: FSMContext):
    if state:
        await state.finish()

    # If in chat
    if m.chat.type != ChatType.PRIVATE:
        await m.answer("😳", reply_markup=types.ReplyKeyboardRemove())
        await m.delete()
        return

    # Check if restart
    user = User.Get(m)
    if not user:
        # Create user if not registered in bot
        User.Create(m.from_user)
        user = User.Get(m)

    await m.answer("🚀 Добро пожаловать в Diforce!", reply_markup=Keyboards.MainMenu(user))

    await Bot.set_my_commands([
        BotCommand("start", "Перезагрузить бота")
    ])