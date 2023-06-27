from typing import Union
from aiogram.types import \
    ReplyKeyboardMarkup as Keyboard, \
    KeyboardButton as Button, \
    InlineKeyboardMarkup as IKeyboard, \
    InlineKeyboardButton as IButton
from dotdict import dotdict
from loader import Consts

from services.textService import Texts


class Keyboards:
    @staticmethod
    def backToCategory(cat):
        if not cat:
            return None
        k = IKeyboard(resize_keyboard=True)
        k.row(IButton(Texts.BackButton, callback_data=f"|Catalog:see_cat:{cat['GroupID']}"))
        return k
    
    @staticmethod
    def storeQuantsKb():
        k = IKeyboard()
        k.row(IButton(Texts.HideButton, callback_data=f"|Cart:hide"))
        return k
    
    @staticmethod
    def addedToCart(good):
        k = IKeyboard()
        k.row(IButton(Texts.ChangeAmount, callback_data=f"|Cart:specify_cart_quantity_2:{good.ProductID}"))
        return k
        
        
    
    @staticmethod
    def SearchQuery():
        k = IKeyboard()
        k.row(IButton(Texts.CancelSearchButton, callback_data="|Catalog:cancel_search"))
        return k
    
    @staticmethod
    def startMenu(user=None):
        k = Keyboard(resize_keyboard=True)
        k.row(Texts.BigSearch)
        k.row()
        k.insert(Texts.CatalogButton)
        k.insert(Texts.CartButton)
        k.row(Texts.Profile)
        if user and (user.is_admin or 'admin' in user.roles):
            k.row(Texts.AdminMenuButton)
        if user and (not user.is_authenticated):
            k.row(Texts.AuthButton)
        return k

    @staticmethod
    def OrderHistory(orders, diforce_user_id, start=0):
        kb = IKeyboard(row_width=2)
        # Замените эту строку на реальные заказы пользователя из базы данных
        for order in orders[start:start+20]:
            kb.insert(IButton(f"Заказ №{order.id}", callback_data=f"see_order:{order.id}:{diforce_user_id}"))
        if len(orders) > 20:
            kb.row()
            kb.insert(IButton("◀️ Предыдущие", callback_data=f"profile:orders_history:{start - 20}"))
            kb.insert(IButton("▶️ Следующие", callback_data=f"profile:orders_history:{start + 20}"))
        kb.row(IButton("Назад", callback_data="profile"))
        return kb

    @staticmethod
    def Profile(user):
        k = IKeyboard()
        if user['is_authenticated']:
            k.add(IButton(f"История заказов", callback_data=f"profile:orders_history"))
        k.row(IButton(Texts.OptPricesFileButton, url="https://opt.diforce.ru"))
        
        if user['is_authenticated']:
            k.row(IButton(Texts.LogoutButton, callback_data=f"profile:logout_popup"))
        k.row(IButton(Texts.HideButton, callback_data=f"profile:hide"))
        return k
    
    
    @staticmethod
    def OrderInfo(order):
        k = IKeyboard(row_width=2)
        # k.row(IButton("Повторить заказ", callback_data=f"repeat_order:{order.id}"))
        k.row(IButton("Назад", callback_data="profile:orders_history"))
        return k

    @staticmethod
    def catalog(categories, start_ind=0):
        k = IKeyboard(row_width=3)
        k.row(IButton(Texts.SearchButton,
                         callback_data="|Catalog:search:None"))
        for catID in list(categories.keys())[start_ind:start_ind+20]:
            k.row(IButton(categories[catID]['GroupName'],
                             callback_data=f"|Catalog:see_cat:{catID}"))
            
        if len(categories) > 20:
            k.row()
            k.insert(IButton("⬅️", callback_data=f"|Catalog:root_categories:{start_ind-20}"))
            k.insert(IButton("➡️", callback_data=f"|Catalog:root_categories:{start_ind+20}"))
        return k

    @staticmethod
    def category(category, goods=False):
        k = IKeyboard(row_width=2)
        k.insert(IButton(Texts.SearchButton,
                         callback_data=f"|Catalog:search:{category['GroupID']}"))
        for subcat in list(category['Subgroups'].values()):
            k.row(IButton(subcat['GroupName'],
                             callback_data=f"|Catalog:see_cat:{subcat['GroupID']}"))
        # Goods in category button
        if goods:
            k.row(IButton(Texts.CategoryGoodsButton,
                  callback_data=f"|Catalog:see_cat_goods:{category['GroupID']}"))
        
        # Brand filter
        k.row()
        k.insert(IButton(Texts.BrandFilter,
                      callback_data=f"|Catalog:brand_filter:{category['GroupID']}"))
        # Price filter
        k.insert(IButton(Texts.PriceFilter,
                      callback_data=f"|Catalog:price_filter:{category['GroupID']}"))
        # Back button
        k.row(IButton(Texts.BackButton,
                      callback_data=f"|Catalog:main"))
        return k

    @staticmethod
    def categoryGoods(cat, goods, head_cat=None):
        k = IKeyboard(row_width=3)
        k.insert(IButton(Texts.SearchButton,
                         callback_data=f"|Catalog:search:{cat['GroupID']}"))
        for good in goods:
            k.row(IButton(good['ProductName'],
                             callback_data=f"|Catalog:see_good:{good['ProductID']}"))
        
        # Brand filter
        k.row()
        k.insert(IButton(Texts.BrandFilter,
                      callback_data=f"|Catalog:brand_filter:{cat['GroupID']}"))
            
        # Price filter
        k.insert(IButton(Texts.PriceFilter,
                      callback_data=f"|Catalog:price_filter:{cat['GroupID']}"))
        
        # Back button
        if head_cat:
            k.row(IButton(Texts.BackButton,
                        callback_data=f"|Catalog:see_cat:{head_cat}"))
        else:
            k.row(IButton(Texts.BackButton,
                        callback_data=f"|Catalog:main"))
        return k
    
    @staticmethod
    def filteredGoods(cat, goods, req_id, start_index=0, head_cat=None):
        k = IKeyboard(row_width=3)
        # Search
        k.insert(IButton(Texts.SearchButton,
                         callback_data=f"|Catalog:search:{req_id}"))
        
        for good in goods[start_index:start_index+20]:
            k.row(IButton(good['ProductName'],
                             callback_data=f"|Catalog:see_good:{good['ProductID']}"))
            
        
        # Brand filter
        k.row()
        k.insert(IButton(Texts.BrandFilter,
                      callback_data=f"|Catalog:brand_filter:{req_id}"))
            
        # Price filter
        k.insert(IButton(Texts.PriceFilter,
                      callback_data=f"|Catalog:price_filter:{req_id}"))
        
            
        k.row()
        # Prev goods
        if len(goods) > 20 and start_index > 0:
            k.insert(IButton("⬅️",
                      callback_data=f"|FilteredGoods:left:{req_id}:{start_index}"))
        if cat:
            # Back button
            k.insert(IButton(Texts.QuitButton,
                        callback_data=f"|Catalog:see_cat:{head_cat if head_cat is not None else cat['GroupID']}"))
        else:
            k.insert(IButton(Texts.QuitButton,
                        callback_data=f"|Catalog:main"))
        
        # Next goods
        if len(goods) > 20 and start_index < len(goods) - 20:
            k.insert(IButton("➡️",
                      callback_data=f"|FilteredGoods:right:{req_id}:{start_index}"))
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
    def PriceFilterMessage(filter_type="price"):
        k = IKeyboard(row_width=1)
        k.row(IButton(Texts.Cancel, callback_data=f"|Catalog:cancel_filter:{filter_type}"))
        return k
    
    @staticmethod
    def BrandFilter(all_brands, selected_brands, req: None):
        k = IKeyboard()
        for x in all_brands:
            k.insert(IButton(('☑️' if x not in selected_brands else '✅ ') + x, callback_data=f"|Catalog:brand_filter_choose:{x}"))
        if req and 'BrandFilter' in req['AppliedFilters']:
            k.row(IButton(Texts.CancelFilter, callback_data=f"|Catalog:cancel_filter:brand"))
        if selected_brands != []:
            k.row(IButton(Texts.Show, callback_data=f"|Catalog:brand_filter_show"))
        k.row(IButton(Texts.Cancel, callback_data=f"|Catalog:cancel_filter:brand"))
        return k
        
        

    @staticmethod
    def goodOptions(user, good, media_group_message_id=None):
        k = IKeyboard(row_width=3)
        if good['ProductID'] not in user['cart']:
            k.row(IButton(Texts.AddToCartButton,
                callback_data=f"|Good:add_to_cart:{good['ProductID']}:{media_group_message_id}"))
        else:
            k.row()
            k.insert(IButton(Texts.DecrementButton,
                    callback_data=f"|Cart:dec_count:{good['ProductID']}:{media_group_message_id}"))
            k.insert(IButton(Texts.RemoveButton + " Удалить",
                    callback_data=f"|Cart:remove_from_cart_2:{good['ProductID']}:{media_group_message_id}"))
            k.insert(IButton(Texts.IncrementButton,
                    callback_data=f"|Cart:inc_count:{good['ProductID']}:{media_group_message_id}"))
            k.row(IButton(Texts.SpecifyCartQuantity2, callback_data=f"|Cart:specify_cart_quantity_2:{good['ProductID']}:{media_group_message_id}"))
        
        k.row(IButton(Texts.FoundCheaperButton,
              callback_data=f"|Good:found_cheaper:{good['ProductID']}"))
        # k.row(IButton(Texts.StoreQuantsButton,
        #       callback_data=f"|Good:store_quants:{good['ProductID']}"))
        k.row(IButton(Texts.ShowPictures,
              callback_data=f"|Good:see_other_photos:{good['ProductID']}:{media_group_message_id}"))
        k.row(IButton(Texts.HideButton, callback_data=f"|Good:hide:{media_group_message_id}"))
        return k

    @staticmethod
    def foundCheaperMenu():
        k = Keyboard(resize_keyboard=True)
        k.row(Texts.QuitButton)
        return k

    @staticmethod
    def yourCart(cartItems, start=0):
        k = IKeyboard(row_width=2)
        for cartItemID, cartItem in cartItems[start:start+10]:
            k.row(IButton(cartItem['ProductName'],
                  callback_data=f"|Cart:see_cart_item:{cartItemID}"))
        
        if len(cartItems) > 10:
            k.row()
            k.insert(IButton("◀️ Предыдущие", callback_data=f"|Cart:main:{start-10}"))
            k.insert(IButton("▶️ Следующие", callback_data=f"|Cart:main:{start+10}"))
        
        k.row()
        k.insert(IButton(Texts.ClearCart, callback_data=f"|Cart:clear_all"))
        k.insert(IButton(Texts.MakeAnOrderButton,
              callback_data=f"|OrderActions:make_an_order"))
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
    def CancelCartQuantity2():
        k = IKeyboard(row_width=3)
        k.row(IButton(Texts.Cancel, callback_data=f"|Cart:cancel_scq_2"))
        return k
    
    @staticmethod
    def AdminMenu():
        k = IKeyboard()
        k.add(IButton(Texts.BroadcastButton, callback_data="admin:broadcast"))
        k.add(IButton(Texts.BotUsersButton, callback_data="admin:bot_users"))
        return k
    
    @staticmethod
    def ParseLinks(links):
        from loggerConf import logger
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
            logger.error(f"Can't parse keyboard, {e}")
            return None
        
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
        k = IKeyboard()
        
        k.row(IButton(Texts.BotUsersDefaultButton, callback_data="bot_users:user"))
        for contractTypeCode in Consts.ContractTypes:
            k.row(IButton(Consts.ContractTypes[contractTypeCode], callback_data=f"bot_users:{contractTypeCode}"))
            
        
        k.row(IButton(Texts.BotUsersAdminsButton, callback_data="bot_users:admin"))
        return k
    
    @staticmethod
    def UserInfoFromAdmin(user):
        k = IKeyboard()
        k.row(IButton("История заказов", callback_data=f"operate_user:user_history:{user.id}"))
        
        for contractTypeCode in Consts.ContractTypes:
            k.row(IButton("Назначить тип цен " + Consts.ContractTypes[contractTypeCode], callback_data=f"operate_user:set_opt:{contractTypeCode}:{user.id}"))
        k.row(IButton("Назначить админом", callback_data=f"operate_user:set_admin:{user.id}"))
        return k
    
    @staticmethod
    def ChooseStore(stores: dict):
        k = IKeyboard()
        for store in list(stores.values()):
            k.row(IButton(store['store_name'], callback_data=f"|OrderActions:make_an_order_store:{store['store_id']}"))
            
        k.row(IButton(Texts.BackButton, callback_data=f"|Cart:back"))
        return k
    
    @staticmethod
    def Popup(success_path: str):
        k = IKeyboard()
        k.insert(IButton(Texts.No, callback_data=f"|just_hide|"))
        k.insert(IButton(Texts.Yes, callback_data=success_path))
        return k
    
    @staticmethod
    def onChatInviteKeyboard(chat_id):
        k = IKeyboard()
        k.insert(IButton("🚀 Использовать чат по умолчанию", callback_data=f"|use_chat:{chat_id}"))
        return k
    
    @staticmethod
    def hideAdditionalPhotos(sessionID):
        k = IKeyboard()
        k.insert(IButton("➖ Скрыть ➖", callback_data=f"|Good:hide:{sessionID}"))
        return k
    
    
    
    @staticmethod
    def ConfirmOrder(pay_method=None, deliv_method=None):
        k = IKeyboard()
        k.row(IButton("💰 Наличные" + (' ✅' if pay_method == 'cash' else ''), callback_data=f"|OrderActions:choose_pay_method:cash"))
        k.insert(IButton("💸 Перевод" + (' ✅' if pay_method == 'transfer' else ''), callback_data=f"|OrderActions:choose_pay_method:transfer"))
        k.insert(IButton("💳 Безнал" + (' ✅' if pay_method == 'non_cash' else ''), callback_data=f"|OrderActions:choose_pay_method:non_cash"))
        
        k.row(IButton("🚗 Самовывоз" + (' ✅' if deliv_method == 'self_pickup' else ''), callback_data=f"|OrderActions:choose_deliv_method:self_pickup"))
        k.insert(IButton("🚛 Доставка" + (' ✅' if deliv_method == 'delivery' else ''), callback_data=f"|OrderActions:choose_deliv_method:delivery"))
        
        k.row(IButton("⭐ Оформить заказ", callback_data=f"|OrderActions:make_an_order_store"))
        k.row(IButton(Texts.BackButton, callback_data=f"|Cart:back"))
        return k
    
    @staticmethod
    def DelivAddress(user, is_delivery, deliv_address_id=None):
        k = IKeyboard()
        for address in user['addresses']:
            k.row(IButton(address['Name'] + (" ✅" if deliv_address_id == address['ID'] else ''), callback_data=f"|OrderActions:choose_address:{address['ID']}"))
        k.row(IButton("➕ Добавить адресс", callback_data=f"|OrderActions:add_deliv_address"))
        k.row(IButton("☑️ Выбрать метод доставки курьером" if not is_delivery else "✅ Выбрана доставка курьером", callback_data=f"|OrderActions:choose_deliv_method:delivery_true"))
        k.row(IButton(Texts.BackButton, callback_data=f"|OrderActions:confirm_order"))
        return k
    
    @staticmethod
    def back(path):
        k = IKeyboard()
        k.row(IButton(Texts.BackButton, callback_data=path))
        return k
        