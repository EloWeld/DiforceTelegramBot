from aiogram.types import \
    ReplyKeyboardMarkup as Keyboard, \
    KeyboardButton as Button, \
    InlineKeyboardMarkup as IKeyboard, \
    InlineKeyboardButton as IButton
from dotdict import dotdict

class Keyboards:
    @classmethod
    def MainMenu():
        k = Keyboard(resize_keyboard=True)
        k.row("Товары")
        return k