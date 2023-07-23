from collections import OrderedDict
import copy
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ParseMode
import loguru
from etc.filters import Admin
from handlers.start import prepareUserToPrint
from loader import MDB, Consts, dp, bot
from etc.keyboards import Keyboards
from services.goodsService import GoodsService
from services.textService import Texts
from aiogram.dispatcher.filters.state import State, StatesGroup
from loggerConf import logger
from services.userService import UserService
from utils import split_long_text

def swap_order(dict_cats, key1, key2):
    dict_cats[key1]['order'], dict_cats[key2]['order'] = dict_cats[key2]['order'], dict_cats[key1]['order']


class Mailing(StatesGroup):
    content = State()
    links = State()
    confirm = State()
    
selected_categories_dict = {'cats':[]}
@dp.callback_query_handler(lambda call: call.data.startswith("admin:"), state="*")
async def process_admin_callback(c: types.CallbackQuery, state: FSMContext):
    global selected_categories_dict
    action = c.data.split(":")[1]
    user = UserService.Get(c.from_user.id)
    t1 = "Укажите новый порядок выбрав категорию, а потом переместив её стрелочками"
    
    if action == "broadcast":
        await c.message.answer(Texts.EnterBroadcastContent, reply_markup=Keyboards.CancelBroadcast())
        await Mailing.content.set()
        
        
    elif action == "sel_category_for_move":
        selected_cat = c.data.split(":")[2]
        await state.update_data(selected_cat=selected_cat)
        
        await c.message.edit_text(t1, reply_markup=Keyboards.adminChangeCatalog(selected_categories_dict['cats'], user, selected_cat))
    elif action == "move_category_up":
        selected_cat = (await state.get_data()).get('selected_cat', None)
        # Найдите категорию, которая находится выше
        previous_cat = None
        for cat, data in selected_categories_dict['cats'].items():
            if data['order'] == selected_categories_dict['cats'][selected_cat]['order'] - 1:
                previous_cat = cat
                break
        if previous_cat:
            swap_order(selected_categories_dict['cats'], selected_cat, previous_cat)

        selected_categories_dict['cats'] = OrderedDict(sorted(selected_categories_dict['cats'].items(), key=lambda x: x[1]['order']))
        await c.message.edit_text(t1, reply_markup=Keyboards.adminChangeCatalog(selected_categories_dict['cats'], user, selected_cat))

    elif action == "move_category_down":
        selected_cat = (await state.get_data()).get('selected_cat', None)
        # Найдите категорию, которая находится ниже
        next_cat = None
        for cat, data in selected_categories_dict['cats'].items():
            if data['order'] == selected_categories_dict['cats'][selected_cat]['order'] + 1:
                next_cat = cat
                break
        if next_cat:
            swap_order(selected_categories_dict['cats'], selected_cat, next_cat)

        selected_categories_dict['cats'] = OrderedDict(sorted(selected_categories_dict['cats'].items(), key=lambda x: x[1]['order']))
        await c.message.edit_text(t1, reply_markup=Keyboards.adminChangeCatalog(selected_categories_dict['cats'], user, selected_cat))
    elif action == "change_catalog_order_next":
        start_index = c.data.split(":")[2]
        selected_cat = (await state.get_data()).get('selected_cat', None)
        await c.message.edit_text(t1, reply_markup=Keyboards.adminChangeCatalog(selected_categories_dict['cats'], user, selected_cat, start_ind=start_index))
        
    elif action == "change_catalog_order":
        categories = MDB.Settings.find_one(dict(id="Catalog"))['catalog']
        # Сортировка словаря по значению поля 'order'
        sorted_items = sorted(categories.items(), key=lambda x: x[1]['order'])
        
        # Преобразование отсортированного списка кортежей обратно в словарь
        categories = OrderedDict(sorted_items)
        selected_categories_dict['cats'] = categories
        selected_cat = (await state.get_data()).get('selected_cat', None)
        await c.message.edit_text(t1, reply_markup=Keyboards.adminChangeCatalog(categories, user, selected_cat))
        
    elif action == "save_categories_order":
        MDB.Settings.update_one({"id": "Catalog"}, {"$set": dict(catalog=selected_categories_dict['cats'])})
        await c.answer("✅ Изменения соханены! ✅")
            
        categories = GoodsService.GetCategoriesTree()

        await c.message.edit_text(Texts.CatalogMessage, reply_markup=Keyboards.catalog(categories, user))
        
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
                logger.error(f"Error sending message to user {user.chat_id}: {e}")

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
        

    if action in ['admin', 'user'] + list(Consts.ContractTypes):
        if action in list(Consts.ContractTypes):
            users = [user for user in UserService.All() if user.opt == action]
            users_text = f"Список пользователей с ролью {Consts.ContractTypes[action]}:\n\n"
        elif action == "user":
            users = [user for user in UserService.All() if (user.roles == ["user"] or user.opt in [None]) and 'admin' not in user.roles and not user.is_admin]
            users_text = f"Список пользователей с ролью Пользователь:\n\n"
        elif action == "admin":
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
        