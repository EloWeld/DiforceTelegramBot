import re
import loguru
from loader import MDB, bot
from services.textService import Texts
from services.userService import UserService


async def notifyAdmins(text: str):
    for admin in UserService.Admins():
        try:
            await bot.send_message(admin['id'], text)
        except Exception as e:
            loguru.logger.error(f"Can't send message to admin: {e}")

def split_long_text(text: str, max_length: int = 4000):
    parts = []
    while len(text) > max_length:
        split_position = text.rfind('\n', 0, max_length)
        if split_position == -1:
            split_position = max_length
        part = text[:split_position]
        parts.append(part)
        text = text[split_position:]
    parts.append(text)
    return parts


def prepareUserToPrint(xUser):
    xUser.roles = ', '.join([Texts.rus(x) for x in xUser.roles])
    xUser.opt = Texts.rus(xUser.opt)
    return xUser

def cutText(text: str, limit: int):
    if len(text) > limit:
        return text[:limit-3] + "..."
    else:
        return text
    

def prepareGoodItemToSend(good):
    """Prepare cart item message text for sending."""
    good['PriceType'] = "МЕЛКИЙ ОПТ" if good['Price'] == good['PriceOptSmall'] else "СРЕДНИЙ ОПТ" if good['Price'] == good['PriceOptMiddle'] else "КРУПНЫЙ ОПТ" if good['Price'] == good['PriceOptLarge'] else "РОЗНИЦА"
    good['Price'] = f"{good['Price']:,}".replace(',', ' ')
    good['ProductDescription'] = cutText(good['ProductDescription'], 3500)
    messageText = Texts.GoodCard.format(**good)
    print(messageText)
    return messageText
    
    

def prepareCartItemToSend(good, cartItem):
    """Prepare cart item message text for sending."""
    good['PriceType'] = "МЕЛКИЙ ОПТ" if good['Price'] == good['PriceOptSmall'] else "СРЕДНИЙ ОПТ" if good['Price'] == good['PriceOptMiddle'] else "КРУПНЫЙ ОПТ" if good['Price'] == good['PriceOptLarge'] else "РОЗНИЦА"
    good['Price'] = f"{good['Price']:,}".replace(',', ' ')
    messageText = Texts.GoodCard.format(
        **good) + Texts.CartItemMessage.format(**cartItem)
    return messageText

def format_phone_number(phone_number):
    # Удаление всех символов, кроме цифр
    phone_number = ''.join(filter(str.isdigit, phone_number))

    # Проверка длины номера телефона
    if len(phone_number) == 10:
        # Добавление префикса "+7"
        phone_number = "+7" + phone_number
    elif len(phone_number) == 11:
        # Проверка префикса и замена, если требуется
        if phone_number.startswith("8"):
            phone_number = "+7" + phone_number[1:]
        elif not phone_number.startswith("+7"):
            phone_number = "+7" + phone_number[1:]
    elif len(phone_number) == 12:
        # Проверка префикса и замена, если требуется
        if phone_number.startswith("8"):
            phone_number = "+7" + phone_number[2:]
        elif not phone_number.startswith("+7"):
            phone_number = "+7" + phone_number[2:]
    
    return phone_number

def format_fio(fio):
    fio = fio.upper()
    # Удаление слов
    words_to_remove = ["ИП", "ИНДИВИДУАЛЬНЫЙ ПРЕДПРИНЕМАТЕЛЬ", "ООО", "ОБЩЕСТВО С ОГРАНИЧЕНОЙ ОТВЕТСТВЕННОСТЬЮ"]
    pattern_words = r'\b(?:{})\b'.format('|'.join(words_to_remove))
    fio = re.sub(pattern_words, '', fio)

    # Удаление кавычек, знаков препинания, специальных символов (кроме пробела)
    pattern_symbols = r'[^\w\s]'
    fio = re.sub(pattern_symbols, '', fio)

    # Удаление двойных пробелов
    fio = re.sub(r'\s+', ' ', fio)

    # Удаление пробелов по краям
    fio = fio.strip()
    return fio