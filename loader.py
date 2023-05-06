import asyncio
import loguru
from pymongo import MongoClient
import os
import platform
from os.path import join, dirname
from dotenv import load_dotenv
from loguru import logger

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

# Load dotenc
dotenv_path = join(dirname(__file__), '.env')
load_dotenv()

# Loader constants
MONGO_CREDENTIALS = os.environ["MongoDB_Credentials"]
MONGO_DB_NAME = os.environ["MongoDB_DatabaseName"]
REQUESTS_TIMEOUT = 8
# Arrghh
message_id_links={}


# Initialize MongoDB

MDB = MongoClient(MONGO_CREDENTIALS).get_database(MONGO_DB_NAME)


class ConstantsMetaClass(type):
    def __getattr__(cls, key):
        doc = MDB.Settings.find_one(dict(id="Constants"))
        if not doc:
            doc = MDB.Settings.insert_one(dict(id="Constants"))
        # If key in constants
        if key in doc:
            return doc[key]

        raise AttributeError(key)

    def __str__(cls):
        return 'Const %s' % (cls.__name__,)


class Consts(metaclass=ConstantsMetaClass):
    pass


# Initialize Telegram bot
bot = Bot(Consts.BotToken, parse_mode=ParseMode.HTML)
ms = MemoryStorage()
dp = Dispatcher(bot, storage=ms)
# ===============================


def onBotStartup():
    from utils import notifyAdmins
    logger.info(f"Bot started! https://t.me/{Consts.BotUsername}")
    asyncio.get_event_loop().create_task(notifyAdmins(f"🤖 Запущен!"))
