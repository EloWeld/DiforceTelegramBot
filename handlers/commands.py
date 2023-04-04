from io import BytesIO
import os
import loguru
import requests
from etc.filters import AntiSpam
from etc.keyboards import Keyboards
from loader import MDB, dp, bot

from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, CommandStart
from aiogram.types import Message, ChatType, BotCommand, InputFile
from services.textService import Texts

from services.userService import UserService
from services.xlsxService import XLSXService

####################################################################
###  ▄▀█ █▀▄ █▀▄▀█ █ █▄░█   █▀▀ █▀█ █▀▄▀█ █▀▄▀█ ▄▀█ █▄░█ █▀▄ █▀  ###
###  █▀█ █▄▀ █░▀░█ █ █░▀█   █▄▄ █▄█ █░▀░█ █░▀░█ █▀█ █░▀█ █▄▀ ▄█  ###
####################################################################
admin_commands = dict(
    updateTexts = "Обновляет текста на те что изменены в БД",
    priceList="Отсылает прайс-лист документ для отповых клиентов",
    catalogToExcel="Генерирует xlsx всех товаров из базы",
)

@dp.message_handler(Command("updateTexts"), AntiSpam(), state="*")
async def _(m: Message, command: Command.CommandObj, state: FSMContext):
    if state:
        await state.finish()
    user = UserService.Get(m.from_user.id)
    if 'admin' in user.roles or user.is_admin:
        loguru.logger.info(f"Updating text in databse with defaults")

        MDB.Settings.update_one(dict(id="Texts"), {"$set": Texts.ALL})
        await m.answer("Готово")

        loguru.logger.success(f"✅ Done")

@dp.message_handler(Command("priceList"), AntiSpam(), state="*")
async def get_price_list(m: Message, command: Command.CommandObj, state: FSMContext):
    if state:
        await state.finish()
        
    user = UserService.Get(m.from_user.id)
    loguru.logger.info(f"Sending price opt list to user: {user.id}|@{user.username}")
    response = requests.get("https://diforce.ru/price.xlsx")
    if response.status_code == 200:
        print(response.content)
        with open("pricesOpt.xlsx", 'wb') as o:
            o.write(response.content)

        await bot.send_document(chat_id=m.chat.id, document=InputFile('pricesOpt.xlsx'))
    else:
        await m.answer("🕸️ Не удалось загрузить файл. Пожалуйста, попробуйте позже.")
    
        

@dp.message_handler(Command("catalogToExcel"), AntiSpam(), state="*")
async def get_price_list(m: Message, command: Command.CommandObj, state: FSMContext):
    if state:
        await state.finish()
        
    user = UserService.Get(m.from_user.id)
    if "admin" in user.roles or user.is_admin:
        loguru.logger.info(f"Generating price list xlsx file for admin")
        
        # Отправка сообщения "⏳ Файл генерируется"
        generating_message = await m.reply("⏳ Файл генерируется")
        
        file_name = XLSXService.generate_price_xlsx()
        with open(file_name, "rb") as file:
            await m.reply_document(document=InputFile(file), caption="Вот ваш прайс-лист в формате xlsx.")
        
        # Удаление сообщения "⏳ Файл генерируется"
        await generating_message.delete()
        
        # Удаление файла после отправки
        os.remove(file_name)
        
        loguru.logger.success(f"✅ Price list xlsx file sent")

@dp.message_handler(Command("help"), AntiSpam(), state="*")
async def help_admin(m: Message, command: Command.CommandObj, state: FSMContext):
    if state:
        await state.finish()
    user = UserService.Get(m.from_user.id)
    if "admin" in user.roles or user.is_admin:
        help_text = "Список админ-команд:\n\n"
        for cmd, description in admin_commands.items():
            help_text += f"/{cmd} - {description}\n"
        await m.reply(help_text)