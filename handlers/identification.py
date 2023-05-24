from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, ChatType, Message
from aiogram.dispatcher.filters import Text, ChatTypeFilter
from aiogram.dispatcher.filters.state import State, StatesGroup
from etc.filters import AntiSpam
from etc.keyboards import Keyboards
from loader import MDB, dp
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from services.goodsService import GoodsService

from services.oneService import OneService
from services.textService import Texts
from services.userService import UserService
from utils import format_phone_number

# задание состояний FSM
class Form(StatesGroup):
    phone_email = State()        # номер телефона/email
    full_name = State()          # полное наименование организации
    inn = State()                # ИНН организации (если есть)


@dp.message_handler(Text(Texts.AuthButton), AntiSpam(), ChatTypeFilter(ChatType.PRIVATE), state="*")
async def _(m: Message, state: FSMContext):
    if state:
        await state.finish()
    
    await m.answer(Texts.PleaseFillForm)
    
    await m.answer("Напиши свой номер телефона/email для входа на сайт:")

    # переход в состояние phone_email для получения номера телефона/email
    await Form.phone_email.set()


# обработчик ответа на вопрос "Номер телефона/email для входа на сайт"
@dp.message_handler(state=Form.phone_email)
async def process_phone_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if "@" in message.text:
            data['email'] = message.text
        else:
            data['phone'] = format_phone_number(message.text)

        # отправляем следующий вопрос
        await message.answer("Введите полное наименование организации/физ лица:")

        # переход в состояние full_name для получения полного наименования организации
        await Form.full_name.set()


# обработчик ответа на вопрос "Ваше полное наименование, например ООО Рога и Копыта"
@dp.message_handler(state=Form.full_name)
async def process_full_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_name'] = message.text

        # отправляем следующий вопрос
        await message.answer("Введите ИНН+КПП организации (Если нет КПП - отправьте просто ИНН. Если вовсе нет ИНН - введите 0):")

        # переход в состояние inn для получения ИНН организации
        await Form.inn.set()

from fuzzywuzzy import fuzz
# обработчик ответа на вопрос "Ваш ИНН если есть"
@dp.message_handler(state=Form.inn)
async def process_inn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user = UserService.Get(message.from_user.id)
        if message.text != "0" and message.text.strip().isdigit():
            data['inn+kpp'] = message.text
        
        # ищем информацию в базе данных
        d_users = MDB.DiforceUsers.find()
        sameUsers = []
        for d_user in d_users:
            cond = True
            if 'inn+kpp' in data and 'INN' in d_user:
                cond = cond and data['inn+kpp'].split('+')[0] == d_user['INN']
            if 'full_name' in data and 'FullName' in d_user:
                prob = fuzz.partial_ratio(format_fio(data['full_name']), format_fio(d_user['FullName']))
                cond = cond and  prob > 90
            if 'phone' in data and 'Phone' in d_user:
                cond = cond and data['phone'] == d_user['Phone']
            if 'email' in data and 'Email' in d_user:
                cond = cond and data['email'].replace(' ', '') == d_user['Email'].replace(' ', '').replace('>', '').replace('<', '')
                
            if cond:
                sameUsers.append(d_user)
                
                
        t = "Спасибо! Вы заполнили анкету. Вот ваши данные:\n\n" \
                            f"Номер телефона/email: {data['phone'] if 'phone' in data else data['email'] if 'email' in data else '?'}\n" \
                            f"Полное наименование: {data['full_name']}\n"
        if 'inn+kpp' in data:
            t += f"ИНН+КПП организации: {data['inn+kpp']}\n"
            
        await message.answer(t)
        if len(sameUsers) <= 3 and len(sameUsers) > 0:
            print(sameUsers)
            user = UserService.Get(message)
            user['is_authenticated'] = True
            user['identification_data'] = dict(data)
            user['diforce_data'] = sameUsers[0]
            
            await message.answer(f"✅ Спасибо! Вы идентифицированы!", reply_markup=Keyboards.startMenu(user))
            
            if user['diforce_data']['ContractType'] in ["МЕЛКООПТОВААЯ", "ОПТОВАЯ"]:
                user['roles'] = list(set(user['roles']+["SmallOpt"]))
                user['opt'] = "SmallOpt"
            elif user['diforce_data']['ContractType'] in ["СПЕЦ ЦЕНА ОПТОВАЯ"]:
                user['roles'] = list(set(user['roles']+["MiddleOpt"]))
                user['opt'] = "MiddleOpt"
            elif user['diforce_data']['ContractType'] == "КРУПНЫЙ ОПТ":
                user['roles'] = list(set(user['roles']+["LargeOpt"]))
                user['opt'] = "LargeOpt"
            else:
                user['opt'] = "Retail"
            
            UserService.Update(user)
        else:
            await message.answer("❌ Вы не идентифицированы. Видимо вы ввели неверные данные либо пользователей с такими данными несколько", reply_markup=Keyboards.startMenu(user))
        # завершаем состояние FSM и сохраняем данные в базе
        await state.finish()