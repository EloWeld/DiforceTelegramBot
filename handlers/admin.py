from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ParseMode
import loguru
from etc.filters import Admin
from handlers.start import prepareUserToPrint
from loader import MDB, Consts, dp, bot
from etc.keyboards import Keyboards
from services.textService import Texts
from aiogram.dispatcher.filters.state import State, StatesGroup

from services.userService import UserService
from utils import split_long_text


class Mailing(StatesGroup):
    content = State()
    links = State()
    confirm = State()
    

@dp.callback_query_handler(lambda call: call.data.startswith("admin:"), state="*")
async def process_admin_callback(c: types.CallbackQuery, state: FSMContext):
    action = c.data.split(":")[1]

    if action == "broadcast":
        await c.message.answer(Texts.EnterBroadcastContent, reply_markup=Keyboards.CancelBroadcast())
        await Mailing.content.set()
    elif action == "cancel_broadcast":
        await state.finish()
        await c.message.answer(Texts.BroadcastCanceled)
        await c.message.delete()
    elif action == "bot_users":
        await c.message.answer(Texts.BotUsersMessage, reply_markup=Keyboards.BotUsersTypes())
    else:
        await c.answer("Неизвестная команда", show_alert=True)


@dp.callback_query_handler(lambda call: call.data.startswith("operate_user:"), state="*")
async def process_admin_callback(c: types.CallbackQuery, state: FSMContext):
    action = c.data.split(":")[1]

    if action == "set_opt":
        opt = c.data.split(":")[2]
        xUser = c.data.split(":")[3]
        xUser = UserService.Get(int(xUser))
        xUser.opt = opt
        roleName = opt
        xUser.roles = [x for x in xUser.roles if "Opt" not in x]
        xUser.roles = list(set(xUser.roles + [roleName]))
        UserService.Update(xUser)
        await c.answer("Готово!", show_alert=True)
        xUser = prepareUserToPrint(xUser)
        await c.message.edit_text(Texts.UserInfoAdminFormat.format(user=xUser), 
                           reply_markup=Keyboards.UserInfoFromAdmin(xUser))
    if action == "set_admin":
        xUser = c.data.split(":")[2]
        xUser = UserService.Get(int(xUser))
        xUser.is_admin = not xUser.is_admin
        if xUser.is_admin:
            xUser.roles = list(set(xUser.roles + ["admin"]))
        else:
            xUser.roles = [x for x in xUser.roles if x != "admin"]
        UserService.Update(xUser)
        await c.answer("Готово!", show_alert=True)
        xUser = prepareUserToPrint(xUser)
        await c.message.edit_text(Texts.UserInfoAdminFormat.format(user=xUser), 
                           reply_markup=Keyboards.UserInfoFromAdmin(xUser))


# region broadcast
@dp.message_handler(content_types=[types.ContentType.PHOTO, types.ContentType.TEXT], state=Mailing.content)
async def process_mailing_photo(message: types.Message, state: FSMContext):
    if message.photo:
        photo = message.photo[-1].file_id
        await state.update_data(photo=photo)
    if message.caption:
        caption = message.caption
        await state.update_data(caption=caption)
    if message.text:
        caption = message.text
        await state.update_data(caption=caption)
    await Mailing.links.set()
    
    await message.answer(Texts.BroadcastLinksMessage)


@dp.message_handler(lambda message: message.text and len(message.text.strip()) > 0, state=Mailing.links)
async def process_links(message: types.Message, state: FSMContext):
    try:
        kb = Keyboards.ParseLinks(message.text)
    except Exception:
        kb = None

    await state.update_data(inline_keyboard=kb)
    
    # Отправьте предпросмотр
    data = await state.get_data()
    photo = data.get("photo")
    caption = data.get("caption")
    await message.answer(Texts.PreviewBroadcastMessage)
    if photo:
        preview_msg = await message.answer_photo(photo=photo, caption=caption, reply_markup=kb)
    else:
        preview_msg = await message.answer(text=caption, reply_markup=kb)
    await Mailing.confirm.set()
    await message.answer(Texts.AdminConfirmBroadcastMessage, reply_markup=Keyboards.ConfirmMailing())
    
    
@dp.callback_query_handler(lambda call: call.data.startswith("mailing_confirm:"), Admin(), state=Mailing.confirm)
async def process_mailing_confirm(call: types.CallbackQuery, state: FSMContext):
    action = call.data.split(":")[1]

    if action == "yes":
        # Получите данные из состояния
        data = await state.get_data()
        photo = data.get("photo")
        caption = data.get("caption")
        inline_keyboard = data.get("inline_keyboard")

        # Реализуйте логику для отправки сообщений всем пользователям
        users = UserService.All()
        for user in users:
            try:
                if photo:
                    await bot.send_photo(chat_id=user.id, photo=photo, caption=caption, reply_markup=inline_keyboard)
                else:
                    await bot.send_message(chat_id=user.id, text=caption, reply_markup=inline_keyboard)
            except Exception as e:
                loguru.logger.error(f"Error sending message to user {user.chat_id}: {e}")

        await state.finish()
        await call.message.answer(Texts.BroadcastDone)

    elif action == "no":
        await state.finish()
        await call.message.answer(Texts.BroadcastCanceled)
        
# endregion broadcast


@dp.callback_query_handler(lambda call: call.data.startswith("bot_users:"), Admin())
async def process_mailing_confirm(call: types.CallbackQuery, state: FSMContext):
    action = call.data.split(":")[1]
    def format_user(user):
        if user.username == None:
            return f"<a href='tg://user?id=>{user.id}'>{user.fullname}</a> | <a href='https://t.me/{Consts.BotUsername}?start=user_info_{user.id}'>Инфо</a>"
        else:
            return f"<a href='https://t.me/{user.username}'>{user.fullname}</a> | <a href='https://t.me/{Consts.BotUsername}?start=user_info_{user.id}'>Инфо</a>"
        

    if action in ['SmallOpt','MiddleOpt','LargeOpt', 'admin', 'user']:
        if action == "SmallOpt":
            users = [user for user in UserService.All() if 'SmallOpt' in user.roles or user.opt == "SmallOpt"]
            users_text = f"Список пользователей с ролью Оптовик Мелкий.:\n\n"
        if action == "MiddleOpt":
            users = [user for user in UserService.All() if 'MiddleOpt' in user.roles or user.opt == "MiddleOpt"]
            users_text = f"Список пользователей с ролью Оптовик Средний:\n\n"
        if action == "LargeOpt":
            users = [user for user in UserService.All() if 'LargeOpt' in user.roles or user.opt == "LargeOpt"]
            users_text = f"Список пользователей с ролью Оптовик Крупный:\n\n"
        if action == "user":
            users = [user for user in UserService.All() if (user.roles == ["user"] or user.opt in [None, 'Retail']) and 'admin' not in user.roles and not user.is_admin]
            users_text = f"Список пользователей с ролью Пользователь:\n\n"
        if action == "admin":
            users = [user for user in UserService.All() if 'admin' in user or user.is_admin]
            users_text = f"Список пользователей с ролью Админ:\n\n"
            
        for user in users:
            users_text += format_user(user) + "\n"
            
        await call.answer()
        if len(users_text.strip().split('\n')) <= 2:
            await call.message.answer(Texts.EmptyList, disable_web_page_preview=True)
            return
        text_parts = split_long_text(users_text)
        for part in text_parts:
            await call.message.answer(part, disable_web_page_preview=True)
        