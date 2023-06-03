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

async def tryDelete(msg):
    try:
        await msg.delete()
    except Exception as e:
        loguru.logger.error(f"Can't delete message, doesnt exists anymore")


def prepareUserToPrint(xUser):
    xUser.roles = ', '.join([Texts.rus(x) for x in xUser.roles])
    xUser.opt = Texts.rus(xUser.opt)
    return xUser

def cutText(text: str, limit: int):
    if len(text) > limit:
        return text[:limit-3] + "..."
    else:
        return text
    

def prepareGoodItemToSend(good, user):
    """Prepare cart item message text for sending."""
    good['PriceType'] = user['optText'] if user['optText'] else "РОЗНИЦА"
    good['Price'] = f"{good['Price']:,}".replace(',', ' ')
    good['ProductDescription'] = good['ProductDescription'].replace('<', '‹').replace('>', '›')
    good['ProductName'] = good['ProductName'].replace('<', '‹').replace('>', '›')
    good['ProductDescription'] = cutText(good['ProductDescription'], 3500)
    messageText = Texts.GoodCard.format(**good)
    print(messageText)
    return messageText
    
    

def prepareCartItemToSend(good, cartItem, user):
    """Prepare cart item message text for sending."""
    good['PriceType'] = user['optText'] if user['optText'] else "РОЗНИЦА"
    good['Price'] = f"{good['Price']:,}".replace(',', ' ')
    good['ProductDescription'] = good['ProductDescription'].replace('<', '‹').replace('>', '›')
    good['ProductName'] = good['ProductName'].replace('<', '‹').replace('>', '›')
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


def is_in_group_hierarchy(user_group, target_groups, groups):
    if user_group in target_groups:
        return True
    
    for group in groups:
        if group['GroupID'] == user_group:
            return is_in_group_hierarchy(group['HeadGroupID'], target_groups, groups)

    return False

def process_string(input_string):
    # Заменить все символы, знаки препинания и специальные символы на пробелы
    cleaned_string = re.sub(r'[^\w\s]', ' ', input_string.lower())
    
    # Разбить строку на слова
    words = cleaned_string.split()
    
    # Удалить пустые строки из массива слов
    words = [word for word in words if word.strip()]
    
    return words