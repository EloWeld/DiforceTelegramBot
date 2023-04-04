from etc.filters import AntiSpam
from etc.keyboards import Keyboards
from loader import dp, bot

from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, CommandStart
from aiogram.types import Message, ChatType, BotCommand
from services.textService import Texts

from services.userService import UserService
from utils import prepareUserToPrint


async def parseStartMessage(m: Message):
    if 'user_info_' in m.text:
        user = UserService.Get(m.from_user.id)
        if user.is_admin or 'admin' in user.roles:
            xUser = UserService.Get(m.text.split('user_info_')[1])
            xUser = prepareUserToPrint(xUser)
            
            await m.answer(Texts.UserInfoAdminFormat.format(user=xUser), 
                           reply_markup=Keyboards.UserInfoFromAdmin(xUser))


@dp.message_handler(CommandStart(), AntiSpam(), state="*")
async def _(m: Message, command: Command.CommandObj, state: FSMContext):
    if state:
        await state.finish()
        
    await parseStartMessage(m)

    # Create or UpdateUser
    user = UserService.Get(m.from_user.id)
    if not user:
        user = UserService.Create(m.from_user)
    else:
        UserService.UpdateFromTgUser(m.from_user)

    await m.answer(Texts.StartMessage, reply_markup=Keyboards.startMenu(user))
    await m.delete()

    await bot.set_my_commands([
        BotCommand("start", "Перезагрузить бота"),
        BotCommand("help", "Помощь")
    ])
