import loguru
from loader import MDB

savedTexts = {}


class TextsMetaClass(type):

    __defaultTexts = dict(
        # Start
        StartMessage="Добро пожаловать в Diforce!",
        # Menu buttons
        CatalogButton="🛍️ Каталог",
        CartButton="🛒 Моя корзина",
        OptPricesFileButton="Для оптовиков",
        OptFileMessage="Для оптовиков вот файл",
        # Catalog
        CatalogMessage="🛍️ Каталог товаров",
        CategoryMessage="️️⏺️ Категория {category.GroupName}\n"
                        "*️⃣ Подкатегорий: {subcategories_count}\n"
                        "💠 Товаров в категории: {category_goods_count}",
        SearchButton="🔎 Поиск",
        CategoryGoodsMessage="💠 Товары категории {category.GroupName} ({goods_count})",
        CategoryGoodsButton="🛒 Товары в категории 🛒",

        # Good in catalog
        GoodCard="""
⏺️ Категория: <b>{GroupName}</b>
🔖 Артикул: <b>{ProductArt}</b>

💠 Наименование: <b>{ProductName}</b>
🗄️ Склад: <b>{StoreName}</b>
🎨 Цвет: <b>{ColorEmoji} {ColorName}</b>

💰 Цена: <b>{Price} ₽</b>

📜 Описание: 
<b>{ProductDescription}</b>
""",
        # Good Buttons
        AddToCartButton="🛒 Добавить в корзину",
        FoundCheaperButton="📉 Нашёл дешевле",
        StoreQuantsButton="📦 Наличие на складах",

        # Good suboptions
        AddedToCart="✅ Добавлено в корзину!",
        YourRequestWasSentMessage="Ваше направление отпрпавлено нашим модераторам! Скоро мы на него ответим 😊",
        QuantityInStores="""
Наличие на складах
{store_text}
""",
        QuantityInStoresFormat="<code>{store_name:24} ➖➖➖ {quantity} шт.</code> ",
        # FoundCheaper
        FoundCheaperMessage="🛒 Нашли дешевле?\n🎁 Мы предложим цену ещё лучше. \n⚠️ Закрепи фото или ссылку продавца.\n",
        FoundCheaperAdminMessage="""
Покупатель <a href='tg://user?id={user.id}>{user.username}|{user.fullname}</a> нашёл товар <code>{good.ProductID}</code> дешевле

👤 Комментарий покупателя: <b>{comment}</b>""",

        # Cart
        YourCartMessage="🛒 Ваша корзина\nИтого: <b>{cart_price} ₽</b>\n\n{cart_text}",
        YourCartIsEmpty="🛒 Ваша корзина пуста!",
        CartItemTextFormat="<code>{ProductName:23} ➖➖➖ {Quantity} шт.</code>",
        CartItemMessage="\n\nВ корзине: {Quantity}",
        MakeAnOrderButton="🛎️ Оформить заказ",
        ClickRemovePopup="Чтобы убрать товар из корзины - нажмите \"{btn}\"",
        CartItemRemoved="✅Товар убран из корзины",
        DecrementButton="-1",
        IncrementButton="+1",
        RemoveButton="🗑️",
        
        # Profile
        Profile = "Личный кабинет",
        YourOrderHistory="📜 Ваша история заказов",
        YourOrdersHistoryIsEmpty="📜 Ваша история заказов пуста 💨",

        # Admin
        AdminMenuButton="👑 Админка",
        AdminMenuMessage="Админ-меню",
        BroadcastButton = "Рассылка сообщений",
        BotUsersButton = "Пользователи бота",
        OrdersHistory="Истории заказов",
        
        EnterBroadcastContent="Введите текст рассылки\n\n(Есть возможность приложить фото)",
        CancelBroadcastButton="❌ Отменить рассылку",
        BroadcastLinksMessage="Пришлите ссылки в формате:\n\nТекст кнопки + URL | Текст кнопки + URL\nТекст кнопки + URL\n\nПробелы обязательны!",
        AdminConfirmBroadcastMessage="Подтверждаете рассылку?",
        PreviewBroadcastMessage="⬇️ Ниже предоставлен предпросмотр рассылки",
        BroadcastDone="Рассылка выполнена.",
        BroadcastCanceled="Рассылка отменена.",
        
        BotUsersMessage="Пользователи бота",
        BotUsersDefaultButton="Обычные",
        BotUsersOpt1Button="ОптМелкий",
        BotUsersOpt2Button="ОптСредний",
        BotUsersOpt3Button="ОптКрупный",
        BotUsersAdminsButton="Админы",
        EmptyList="🕸️ Пусто 🕸️",
        UserInfoAdminFormat="""Пользователь {user.fullname}
        
Юзернейм: @{user.username}
Роли: {user.roles}
Опт: {user.opt}

""",

        # Search
        EnterSearchQuery="🔎 Введите ключевые слова для поиска",
        CancelSearchButton="❌ Отменить",
        SearchResults="Результаты поиска ({found_count})",
        SpecifyCartQuantity="✏️ Укажите количество",
        IncorrectQuantity="❌ Некорректное количество",
        
        # Other
        QuitButton="🚪 Выход",
        Cancel="❌ Отменить",
        HideButton="➖Скрыть➖",
        BackButton="◀️ Назад",
    )
    
    def rus(cls, key):
        if key == "SmallOpt":
            return "Мелкий опт"
        if key == "MiddleOpt":
            return "Средний опт"
        if key == "LargeOpt":
            return "Крупный опт"
        if key == "admin":
            return "Админ"
        if key == "user":
            return "Пользователь"
        if key == "None":
            return "Не указано"
        else:
            return key

    def __getattr__(cls, key):
        doc = MDB.Settings.find_one(dict(id="Texts"))
        if not doc:
            doc = MDB.Settings.insert_one(dict(id="Texts"))

        if key in doc:
            loguru.logger.success(f"[TEXTS]: Saved text for key: {key}")
            return doc[key]
        elif key in cls.__defaultTexts:
            t_value = cls.__defaultTexts[key]
            MDB.Settings.update_one(
                dict(id="Texts"), {"$set": {key: t_value}})
            loguru.logger.success(f"[TEXTS]: Saved text for key: {key}")
            return t_value
        elif key == "ALL":
            return cls.__defaultTexts
        else:
            loguru.logger.error(
                f"[TEXTS]: Can't found default text for key \"{key}\"")

        raise AttributeError(key)
    
    def __setitem__(cls, key, value):
        MDB.Settings.update_one(dict(id="Texts"), {"$set": {key: value}})


    def __str__(cls):
        return f'Text {cls.__name__}'


class Texts(metaclass=TextsMetaClass):
    pass
