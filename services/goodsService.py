from typing import Optional, Tuple, Union

import Levenshtein
from etc.helpers import rdotdict
from loader import MDB
from services.oneService import OneService
from dotdict import dotdict
from func_timeout import func_timeout, FunctionTimedOut
from loggerConf import logger

class GoodsService:
    @staticmethod
    def GetTargetPrice(user, good):
        try:
            if user['opt'] == None:
                return good['Price']
            else:
                return good['Price' + user['opt']]
        except Exception as e:
            logger.error(f"{e}, {good}, {user}")

    @staticmethod
    def GetCategoriesTree() -> rdotdict:
        """
        Получает дерево категорий товаров и возвращает его в виде объекта `rdotdict`, содержащего информацию о категориях и подкатегориях.
        """
        result = MDB.Settings.find_one(dict(id="Catalog"))
        result = rdotdict(result['catalog'])
        return result

    @staticmethod
    def GetCategoryByID(category_id, subgroups=[]) -> Optional[rdotdict]:
        if category_id is None:
            return None
        """
        Получает информацию о категории товаров по её идентификатору `category_id` и возвращает объект `rdotdict`, содержащий информацию о категории, или `None`, если категория не найдена.
        """
        if category_id in subgroups:
            return rdotdict(subgroups[category_id])

        for group_id in subgroups:
            subgroups2 = subgroups[group_id]['Subgroups']
            if subgroups2:
                result = GoodsService.GetCategoryByID(category_id, subgroups2)
                if result:
                    return result
        return None
    
    @staticmethod
    def GetGoodByID(good_id, with_images=False) -> Union[Tuple[dotdict, list], dotdict]:
        """
        Получает информацию о товаре по его идентификатору `good_id` и возвращает объект `dotdict`, 
        содержащий информацию о товаре, или кортеж из объекта `dotdict`, содержащего информацию о товаре, 
        и списка изображений товара, если параметр `with_images` равен `True`. 

        Если запрос на получение информации о товаре по идентификатору не завершится в течение 2 секунд, 
        метод возвращает информацию о товаре, полученную из базы данных.
        """
        try:
            good = func_timeout(2, OneService.getGood, args=(good_id, True))
        except FunctionTimedOut:
            logger.error('Time expired')
            
            good = MDB.Goods.find_one(dict(ProductID=good_id))
            
        try:
            good['QtyInStore'] = [x for x in good['QuantityInStores'] if x['store_id'] == "000000001"][0]['quantity']
        except Exception:
            good['QtyInStore'] = 0

        if with_images:
            try:
                images = func_timeout(
                    5, OneService.getGoodImages, args=(good_id,))
            except FunctionTimedOut:
                logger.error('Time expired')
                images = []
            return dotdict(good), images
        return dotdict(good)

    @staticmethod
    def LevenshteinDistance(s1, s2) -> int:
        """
        Вычисляет расстояние Левенштейна между строками `s1` и `s2` и возвращает его значение.
        """
        return Levenshtein.distance(s1, s2)

    @staticmethod
    def SearchCatalog(keyword, threshold=3, group_id=None) -> list:
        """
        Ищет товары в каталоге по ключевому слову `keyword`, используя расстояние Левенштейна с порогом `threshold`. Если параметр `group_id` не указан, метод использует данные о каталоге товаров из сервиса OneService. Если параметр `group_id` указан, метод использует данные о товарах из базы данных. Метод возвращает список товаров, удовлетворяющих критериям поиска.
        """
        if not group_id:
            catalog = OneService.getCatalog(group_id=group_id)
        else:
            catalog = [rdotdict(x) for x in list(MDB.Goods.find())]
        matching_items = []

        for item in catalog:
            distance = GoodsService.LevenshteinDistance(
                item['ProductName'].lower(), keyword.lower())
            if distance <= threshold:
                item['l_distance'] = distance
                matching_items.append(item)

        return sorted(matching_items, key=lambda x: x['l_distance'])

    @staticmethod
    def SpecifyColorEmoji(good):
        """
        Добавляет эмодзи для названий цветов товара в объект `good` в поле `ColorEmoji`.
        """
        good['ColorEmoji'] = ""
        try:
            colors = {
                'розовое золото': '🌸✨',
                'чёрный': '⚫️',
                'черный': '⚫️',
                'белый': '⚪️',
                'красный': '🔴',
                'синий': '🔵',
                'жёлтый': '🟡',
                'зелёный': '🟢',
                'оранжевый': '🟠',
                'фиолетовый': '🟣',
                'красно-черный': '🔴+⚫️',
                'розовый': '🌸',
                'серый': '🔘',
                'бирюзовый': '🐬',
                'серебряный': '🥈',
                'золотой': '🥇',
                'бронзовый': '🥉',
                'бежевый': '🐪',
                'коричневый': '🟫',
                'салатовый': '🥗',
                'светло-серый': '⚪️+🔘',
                'серебристый': '🥈',
                'бело-серый': '⚪️+🔘',
                'фиолетово-розовый': '🟣+🌸',
                'красно-коричневый': '🔴+🟫',
                'серебряно-белый': '🥈+⚪️',
                'темно-синий': '🌑',
                'светло-розовый': '🌸+⚪️',
                'золотистый': '🥇',
                'зеленоватый': '🌿',
                'темно-зеленый': '🌲',
                'беж': '🐪',
                'темно-коричневый': '🐻',
                'малиновый': '🍇',
                'розово-фиолетовый': '🌸+🟣',
                'коралловый': '🐚',
                'лавандовый': '💜',
                'сиреневый': '🌸+🟣',
                'хаки': '🍂',
                'светло-зеленый': '🌱',
                'серо-зеленый': '🌿+🔘',
                'красно-розовый': '🔴+🌸',
                'голубой': '🦋',
                'лимонный': '🍋',
                'бело-голубой': '⚪️+🦋',
                'светло-желтый': '🟡+⚪️',
                'матовый черный': '⚫️+🌫️',
                'матовый серый': '🔘+🌫️',
                'матовый бежевый': '🐪+🌫️',
                'матовый коричневый': '🟫+🌫️',
                'матовый синий': '🔵+🌫️',
                'матовый зеленый': '🟢+🌫️',
                'матовый красный': '🔴+🌫️',
                'матовый белый': '⚪️+🌫️',
                'гранатовый': '🍇',
                'светло-голубой': '🐳',
                'светло-розово-фиолетовый': '🌸+🟣+⚪️',
                'голубовато-серый': '🔘+🦋',
                'серо-синий': '🔵+🔘',
                'лиловый': '🟣',
                'кремовый': '🍦',
                'красно-оранжевый': '🟠+🔴',
                'светло-фиолетовый': '🟣+⚪️',
                'желто-зеленый': '🟢+🟡',
                'красно-розовый': '🔴+🌸',
                'оранжево-желтый': '🟠+🟡',
                'бежево-серый': '🐪+🔘',
                'светло-коричневый': '🟫+⚪️',
                'красно-коричнево-желтый': '🔴+🟫+🟡',
                'баклажановый': '🍆',
                'золотисто-бежевый': '🥇+🐪',
                'фисташковый': '🌿',
                'серо-голубой': '🦋+🔘',
                'бирюзово-зеленый': '🟢+🐬',
                'голубовато-зеленый': '🟢+🦋',
                'молочно-белый': '🍼',
                'персиковый': '🍑',
                'песочный': '🏜',
                'зеленовато-серый': '🔘+🟢',
                'красно-фиолетовый': '🔴+🟣',
                'коричный': '🟫',
                'хаки-зеленый': '🟢+🟫',
                'светло-красный': '🔴+⚪️',
                'темно-серый': '🔘+🌚',
                'светло-бирюзовый': '🟢+⚪️',
                'бирюзовый': '🐬',
                'оливковый': '🫒',
                'бирюзовый': '🟦',
                'светло-лиловый': '🟣+⚪️',
                'лососевый': '🐟',
                'голубой сапфир': '💎',
                'фуксия': '🌸',
                'зеленый чай': '🍵',
                'лайм': '🍋+🟢',
                'красно-коричневый': '🔴+🟫',
                'золотистый': '🏆',
                'бронзовый': '🏅',
                'серебряный': '🥈',
                'белый': '⚪️',
                'черный': '⚫️',
                'коричневый': '🟫',
                'розовый': '🌸',
                'фиолетовый': '🟣',
                'желтый': '🟡',
                'оранжевый': '🟠',
                'зеленый': '🟢',
                'голубой': '🔵',
                'серый': '🔘'}

            if good['ColorName'].lower() in colors:
                good['ColorEmoji'] = colors[good['ColorName'].lower()]
        except Exception as e:
            logger.error(e)
            
        return good['ColorEmoji']
