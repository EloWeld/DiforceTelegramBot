import asyncio
from pymongo import MongoClient
import os
import platform
from os.path import join, dirname
from dotenv import load_dotenv
from loguru import logger

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

if platform.system() == "Windows":
    import pythoncom
    import win32com.client

# Load dotenc
dotenv_path = join(dirname(__file__), '.env')
load_dotenv()

if platform.system() == "Windows":
    # Initializating V83 for connect to 1C
    V83_CONN_STRING = f"Srvr={os.environ['1C_Host']};" \
                        f"Ref={os.environ['1C_DatabaseName']};" \
                        f"Usr={os.environ['1C_Username']};" \
                        f"Pwd={os.environ['1C_Password']};"
    logger.info(f"Initialize COM with creds: {V83_CONN_STRING}")


    pythoncom.CoInitialize()
    V83 = win32com.client.Dispatch("V83.COMConnector").Connect(V83_CONN_STRING)
else:
    V83 = None

# Initialize Telegram bot
bot = Bot(os.environ['TgBotToken'], parse_mode=ParseMode.HTML)
ms = MemoryStorage()
dp = Dispatcher(bot, storage=ms)

# Initialize MongoDB

MDB = MongoClient(os.environ["MongoDB_Credentials"]).get_database("Diforce")
def MDBSettings(key: str):
    return MDB.Settings.find_one(dict())[key]

# ===============================

def onBotStartup():
    from utils import notifyAdmins
    logger.info(f"Bot started! https://t.me/{MDBSettings('BotUsername')}")
    asyncio.get_event_loop().create_task(notifyAdmins(f"🤖 Запущен!"))


