from typing import Union
from aiogram.types import \
    ReplyKeyboardMarkup as Keyboard, \
    KeyboardButton as Button, \
    InlineKeyboardMarkup as IKeyboard, \
    InlineKeyboardButton as IButton
from dotdict import dotdict

from services.textService import Texts


class Keyboards:
    @staticmethod
    def SearchQuery():
        k = IKeyboard(resize_keyboard=True)
        k.row(IButton(Texts.CancelSearchButton, callback_data="|Catalog:cancel_search"))
        return k
    
    @staticmethod
    def startMenu(user=None):
        k = Keyboard(resize_keyboard=True)
        k.row()
        k.insert(Texts.CatalogButton)
        k.insert(Texts.CartButton)
        k.row(Texts.Profile)
        if user and (user.is_admin or 'admin' in user.roles):
            k.row(Texts.AdminMenuButton)
        if user and (not user.is_authenticated):
            k.row(Texts.AuthButton)
        #k.row(Texts.OptPricesFileButton)
        return k

    @staticmethod
    def OrderHistory(orders):
        kb = IKeyboard()
        # Замените эту строку на реальные заказы пользователя из базы данных
        for order in orders:
            kb.add(IButton(f"Заказ №{order.id}", callback_data=f"see_order:{order.id}"))
        kb.add(IButton("Назад", callback_data="back_to_personal_cabinet"))
        return kb

    @staticmethod
    def Profile(user):
        kb = IKeyboard()
        # Замените эту строку на реальные заказы пользователя из базы данных
        kb.add(IButton(f"История заказов", callback_data=f"profile:orders_history"))
        kb.row(IButton(Texts.OptPricesFileButton, url="https://diforce.ru/price.xlsx"))
        return kb
    
    
    @staticmethod
    def OrderInfo(order):
        k = IKeyboard(row_width=2)
        k.row(IButton("Повторить заказ", callback_data=f"repeat_order:{order.id}"),
              IButton("Назад", callback_data="back_to_order_history"))
        return k

    @staticmethod
    def catalog(categories):
        k = IKeyboard(row_width=1)
        k.insert(IButton(Texts.SearchButton,
                         callback_data="|Catalog:search:None"))
        k.row()
        for catID in categories:
            k.insert(IButton(categories[catID]['GroupName'],
                             callback_data=f"|Catalog:see_cat:{catID}"))
        return k

    @staticmethod
    def category(category, goods=False):
        k = IKeyboard(row_width=1)
        k.insert(IButton(Texts.SearchButton,
                         callback_data=f"|Catalog:search:{category['GroupID']}"))
        k.row()
        for subcat in list(category['Subgroups'].values()):
            k.insert(IButton(subcat['GroupName'],
                             callback_data=f"|Catalog:see_cat:{subcat['GroupID']}"))
        # Goods in category button
        if goods:
            k.row(IButton(Texts.CategoryGoodsButton,
                  callback_data=f"|Catalog:see_cat_goods:{category['GroupID']}"))
        # Back button
        k.row(IButton(Texts.PriceFilter,
                      callback_data=f"|Catalog:price_filter:{category['GroupID']}"))
        # Back button
        k.row(IButton(Texts.BackButton,
                      callback_data=f"|Catalog:main"))
        return k

    @staticmethod
    def categoryGoods(cat, goods):
        k = IKeyboard(row_width=1)
        k.insert(IButton(Texts.SearchButton,
                         callback_data=f"|Catalog:search:{cat['GroupID']}"))
        k.row()
        for good in goods:
            k.insert(IButton(good['ProductName'],
                             callback_data=f"|Catalog:see_good:{good['ProductID']}"))
        # Back button
        k.row(IButton(Texts.BackButton,
                      callback_data=f"|Catalog:see_cat:{cat['HeadGroupID']}"))
        return k
    
    @staticmethod
    def SearchResults(goods, group_id=None):
        k = IKeyboard(row_width=1)
        k.row()
        for good in goods:
            k.insert(IButton(good['ProductName'],
                             callback_data=f"|Catalog:see_good:{good['ProductID']}"))
        # Back button
        if group_id:
            k.row(IButton(Texts.BackButton,
                        callback_data=f"|Catalog:see_cat:{group_id}"))
        return k
    
    @staticmethod
    def PriceFilterMessage():
        k = IKeyboard(row_width=1)
        k.row(IButton(Texts.Cancel, callback_data="|Catalog:cancel_filter"))
        return k
        

    @staticmethod
    def goodOptions(good, media_group_message_id: Union[int, None]=None):
        k = IKeyboard(row_width=1)
        k.row(IButton(Texts.AddToCartButton,
              callback_data=f"|Good:add_to_cart:{good['ProductID']}"))
        k.row(IButton(Texts.FoundCheaperButton,
              callback_data=f"|Good:found_cheaper:{good['ProductID']}"))
        k.row(IButton(Texts.StoreQuantsButton,
              callback_data=f"|Good:store_quants:{good['ProductID']}"))
        k.row(IButton(Texts.HideButton, callback_data=f"|Good:hide:{media_group_message_id}"))
        return k

    @staticmethod
    def foundCheaperMenu():
        k = Keyboard(row_width=1)
        k.row(Texts.QuitButton)
        return k

    @staticmethod
    def yourCart(cartItems):
        k = IKeyboard(row_width=1)
        for cartItem in cartItems:
            k.row(IButton(cartItem.ProductName,
                  callback_data=f"|Cart:see_cart_item:{cartItem.ProductID}"))
        k.row(IButton(Texts.MakeAnOrderButton,
              callback_data=f"|Cart:make_an_order"))
        k.row(IButton(Texts.HideButton, callback_data=f"|Cart:hide"))
        return k

    @staticmethod
    def cartItem(cartItem):
        k = IKeyboard(row_width=3)
        k.insert(IButton(Texts.DecrementButton,
                 callback_data=f"|Cart:dec_count:{cartItem.ProductID}"))
        k.insert(IButton(Texts.RemoveButton,
                 callback_data=f"|Cart:remove_from_cart:{cartItem.ProductID}"))
        k.insert(IButton(Texts.IncrementButton,
                 callback_data=f"|Cart:inc_count:{cartItem.ProductID}"))
        
        k.row(IButton(Texts.SpecifyCartQuantity, callback_data=f"|Cart:specify_cart_quantity:{cartItem.ProductID}"))
        k.row(IButton(Texts.BackButton, callback_data=f"|Cart:back"))
        return k

    @staticmethod
    def CancelCartQuantity():
        k = IKeyboard(row_width=3)
        k.row(IButton(Texts.Cancel, callback_data=f"|Cart:cancel_scq"))
        return k
    
    @staticmethod
    def AdminMenu():
        k = IKeyboard()
        k.add(IButton(Texts.BroadcastButton, callback_data="admin:broadcast"))
        k.add(IButton(Texts.BotUsersButton, callback_data="admin:bot_users"))
        return k
    
    @staticmethod
    def ParseLinks(links):
        import loguru
        k = IKeyboard()
        try:
            for group in links.strip().split('\n'):
                if group.strip() == "":
                    continue
                k.row()
                for link in group.split(' | '):
                    text, url = link.split(' + ', 1)
                    k.insert(IButton(text.strip(), url=url.strip()))
            return k
        except Exception as e:
            loguru.logger.error(f"Can't parse keyboard, {e}")
            return False
        
    @staticmethod
    def ConfirmMailing():
        markup = IKeyboard()
        markup.add(IButton("Да", callback_data="mailing_confirm:yes"))
        markup.add(IButton("Нет", callback_data="mailing_confirm:no"))
        return markup
    
    @staticmethod
    def CancelBroadcast():
        markup = IKeyboard()
        markup.add(IButton(Texts.CancelBroadcastButton, callback_data="admin:cancel_broadcast"))
        return markup
        
    
    @staticmethod
    def BotUsersTypes():
        markup = IKeyboard()
        
        markup.row(IButton(Texts.BotUsersDefaultButton, callback_data="bot_users:user"))
        
        markup.row(IButton(Texts.BotUsersOpt1Button, callback_data="bot_users:LargeOpt"))
        markup.row(IButton(Texts.BotUsersOpt2Button, callback_data="bot_users:MiddleOpt"))
        markup.row(IButton(Texts.BotUsersOpt3Button, callback_data="bot_users:LargeOpt"))
        
        
        markup.row(IButton(Texts.BotUsersAdminsButton, callback_data="bot_users:admin"))
        return markup
    
    @staticmethod
    def UserInfoFromAdmin(user):
        k = IKeyboard()
        k.row(IButton("История заказов", callback_data=f"operate_user:user_history:{user.id}"))
        k.row(IButton("Назначить мелкий опт", callback_data=f"operate_user:set_opt:SmallOpt:{user.id}"))
        k.row(IButton("Назначить средний опт", callback_data=f"operate_user:set_opt:MiddleOpt:{user.id}"))
        k.row(IButton("Назначить крупный опт", callback_data=f"operate_user:set_opt:LargeOpt:{user.id}"))
        k.row(IButton("Назначить админом", callback_data=f"operate_user:set_admin:{user.id}"))
        return k
    
    @staticmethod
    def ChooseStore(stores: dict):
        k = IKeyboard()
        for store in list(stores.values()):
            k.row(IButton(store['store_name'], callback_data=f"|Cart:make_an_order_store:{store['store_id']}"))
            
        k.row(IButton(Texts.BackButton, callback_data=f"|Cart:back"))
        return k