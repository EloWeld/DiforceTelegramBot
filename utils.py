import re
import loguru
from loader import MDB, bot
from services.goodsService import GoodsService
from services.textService import Texts
from services.userService import UserService
import re
from loggerConf import logger

def split_message_by_new_line(message, max_length):
    parts = message.split('\n')
    result_parts = []
    current_part = ''

    for part in parts:
        if len(current_part) + len(part) + 1 <= max_length:  # +1 для символа новой строки
            current_part += part + '\n'
        else:
            result_parts.append(current_part)
            current_part = part + '\n'

    if current_part:
        result_parts.append(current_part)

    return result_parts

def format_plural(number, form1, form2, form3):
    if number % 10 == 1 and number % 100 != 11:
        return f"{number} {form1}"
    elif number % 10 in (2, 3, 4) and number % 100 not in (12, 13, 14):
        return f"{number} {form2}"
    else:
        return f"{number} {form3}"

async def notifyAdmins(text: str):
    for admin in UserService.Admins():
        try:
            await bot.send_message(admin['id'], text)
        except Exception as e:
            logger.error(f"Can't send message to admin: {e}")

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
        logger.error(f"Can't delete message, doesnt exists anymore")


def prepareUserToPrint(xUser):
    xUser.roles = ', '.join([Texts.rus(x) for x in xUser.roles])
    xUser.opt = xUser['optText']
    return xUser

def cutText(text: str, limit: int):
    if len(text) > limit:
        return text[:limit-3] + "..."
    else:
        return text
    

def prepareGoodItemToSend(good, user):
    """Prepare cart item message text for sending."""
    good['PriceType'] = user['optText'] if user['optText'] else "РОЗНИЦА"
    good['Price'] = f"{GoodsService.GetTargetPrice(user, good):,}".replace(',', ' ')
    good['ProductDescription'] = good['ProductDescription'].replace('<', '‹').replace('>', '›')
    good['ProductName'] = good['ProductName'].replace('<', '‹').replace('>', '›')
    if "не найден" in good['ColorName']:
        good['ColorName'] = "❌"
    good['ColorName'] = good['ColorName'].replace('<', '‹').replace('>', '›')
    good['ProductDescription'] = cutText(good['ProductDescription'], 3500)
    messageText = Texts.GoodCard.format(**good)
    return messageText
    
    

def prepareCartItemToSend(good, cartItem, user):
    """Prepare cart item message text for sending."""
    good['PriceType'] = user['optText'] if user['optText'] else "РОЗНИЦА"
    good['Price'] = f"{GoodsService.GetTargetPrice(user, good):,}".replace(',', ' ')
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


def getCartPrice(user):
    from services.goodsService import GoodsService
    cart_price = 0
    for cartItemID in user['cart']:
        good = MDB.Goods.find_one(dict(ProductID=user['cart'][cartItemID]['ProductID']))
        x = GoodsService.GetTargetPrice(user, good)
        cart_price += x * user['cart'][cartItemID]['Quantity']
    return cart_price