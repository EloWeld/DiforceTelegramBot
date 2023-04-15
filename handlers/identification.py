from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, ChatType, Message
from aiogram.dispatcher.filters import Text, ChatTypeFilter
from aiogram.dispatcher.filters.state import State, StatesGroup
from etc.filters import AntiSpam
from etc.keyboards import Keyboards
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from services.goodsService import GoodsService

from services.oneService import OneService
from services.textService import Texts
from services.userService import UserService

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
            data['phone'] = message.text

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


# обработчик ответа на вопрос "Ваш ИНН если есть"
@dp.message_handler(state=Form.inn)
async def process_inn(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text != "0" and message.text.strip().isdigit():
            data['inn'] = message.text
        # ищем информацию в базе данных
        sameUsers = OneService.GetUsersByParams(data)
    
        if len(sameUsers) == 1:
            print(sameUsers)
            await message.answer(f"Спасибо! Вы идентифицированы!")
            user = UserService.Get(message)
            user['is_authenticated'] = True
            user['identification_data'] = data
            user['diforce_data'] = sameUsers[0]
            
            if user['diforce_data']['ContractType'] == "МЕЛКООПТОВААЯ":
                user['roles'] = list(set(user['roles']+["SmallOpt"]))
                user['opt'] = "SmallOpt"
            if user['diforce_data']['ContractType'] == "ОПТОВАЯ":
                user['roles'] = list(set(user['roles']+["SmallOpt"]))
                user['opt'] = "SmallOpt"
            if user['diforce_data']['ContractType'] == "КРУПНЫЙ ОПТ":
                user['roles'] = list(set(user['roles']+["SmallOpt"]))
                user['opt'] = "SmallOpt"
            
            UserService.Update(user)
        else:
            await message.answer("Вы не идентифицированы. Видимо вы ввели неверные данные либо пользователей с такими данными несколько")
        # завершаем состояние FSM и сохраняем данные в базе
        await state.finish()
        await message.answer("Спасибо! Вы заполнили анкету. Вот ваши данные:\n\n"
                            f"Номер телефона/email: {data['phone_email']}\n"
                            f"Полное наименование организации: {data['full_name']}\n"
                            f"ИНН организации: {data['inn']}\n")