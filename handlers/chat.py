
import base64
import loguru
from etc.filters import AntiSpam
from etc.helpers import wrap_media
from etc.keyboards import Keyboards
from loader import MDB, dp, bot

from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, CommandStart
from aiogram.types import Message, ChatType, BotCommand
from services.goodsService import GoodsService
from services.textService import Texts

from aiogram.types import Message, ChatType, BotCommand, CallbackQuery, ContentType, MediaGroup, InputFile
from services.userService import UserService

from aiogram.utils.exceptions import BotBlocked, ChatNotFound, UserDeactivated, BotKicked

@dp.callback_query_handler(text_contains="|use_chat:", state="*")
async def _(c: CallbackQuery, state: FSMContext):
    if state:
        await state.finish()
    chat_id = c.data.split(":")[1]
    user = UserService.Get(c)
    
    if user.is_admin or 'admin' in user.roles:
        MDB.Settings.update_one(dict(id="Constants"), {"$set": dict(OrderManagerID=chat_id)})
        await c.answer("Готово!", show_alert=True)
        await c.message.delete()
    
    
@dp.message_handler(content_types=['new_chat_members'])
async def on_chat_member_added(message: types.ChatMemberUpdated):
    new_members = message.new_chat_members
    me = await bot.get_me()
    for member in new_members:
        if member.id == me.id:
            try:
                await bot.send_message(message.chat.id, "Привет! Я ваш новый бот.")
                for admin in UserService.Admins():
                    await bot.send_message(admin.id, f"🔔 Бот добавлен в чат <code>{message.chat.id}</code> с названием <code>{message.chat.title}</code>. Если вы хотите использовать этот чат как чат для уведомлений о заказах - нажмите кнопку ниже", reply_markup=Keyboards.onChatInviteKeyboard(message.chat.id))
            except (BotBlocked, ChatNotFound, UserDeactivated, BotKicked) as e:
                for admin in UserService.Admins():
                    await bot.send_message(admin.id, f"Бот не может отправить сообщения в чат {message.chat.id} из-за ошибки {e}")
