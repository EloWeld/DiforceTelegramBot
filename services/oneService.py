import datetime
from typing import List
import loguru
import requests
from loggerConf import logger
import urllib.parse
from loggerConf import logger
from etc.helpers import rdotdict

from loader import MDB, REQUESTS_TIMEOUT, Consts

def merge_stores(stores, merge_ids, merge_to_id):
    # найдем магазин, в который будут объединены магазины
    merge_to_store = next((store for store in stores if store["store_id"] == merge_to_id), None)

    # если магазин не найден, создадим новый магазин
    if not merge_to_store:
        merge_to_store = {"store_name": "DiForce ОПТОВЫЙ", "store_id": merge_to_id, "quantity": 0}
        stores.append(merge_to_store)

    # объединим магазины в один магазин
    stores_to_remove = []
    for store in stores:
        if store["store_id"] in merge_ids:
            merge_to_store["quantity"] += store["quantity"]
            stores_to_remove.append(store)

    # удаляем объединенные магазины из списка
    for store in stores_to_remove:
        stores.remove(store)

    # вернем обновленный список магазинов
    return stores

def adaptGood(good: dict, goodEntities: List[dict] = None):
    from services.goodsService import GoodsService
    from etc.helpers import rdotdict
    
    good['UpdateTime'] = datetime.datetime.now()
    good['Price'] = good['Price000000005']
    good['ProductArt'] = good['ProductART']
    good['PriceOptSmall'] = good['Price000000004']
    good['PriceOptMiddle'] = good['Price000000003']
    good['PriceOptLarge'] = good['PriceЦБ0000001']
    good['Manufacturer'] = good['Manufacturer'] if good['Manufacturer'] not in ['', 'no name'] else 'Незвестно'
    GoodsService.SpecifyColorEmoji(good)

    if goodEntities:
        good['QuantityInStores'] = [
            dict(store_name=x['StoreName'], store_id=x["StoreID"], quantity=x['Quantity']) for x in goodEntities]
    
    good['QuantityInStores'] = merge_stores(good['QuantityInStores'], ["000000002"], "000000001")
    
    try:
        good['QtyInStore'] = [x for x in good['QuantityInStores'] if x['store_id'] == "000000001"][0]['quantity']
    except Exception:
        good['QtyInStore'] = 0
    
    for x in ["Price000000005",
              "ProductART",
              "Price000000004",
              "Price000000003",
              "PriceЦБ0000001"]:
        del good[x]
    return rdotdict(good)


class OneServiceBase:
    def __init__(self) -> None:
        self.base_endpoint = Consts.OneServiceEndpoint
        self.session = requests.Session()
        self.session.auth = (Consts.OneServiceLogin, Consts.OneServicePassword)
        
    def GetOrdersByUser(self, user):
        r = self.session.get(self.base_endpoint+"getOrdersHistory", params=dict(ClientID=user['diforce_data']['ID']))
        if r.status_code != 200:
            logger.error(
                f"Can't get orders history; Response: {r.text}, Status: {r.status_code}")
        return r.json()
    
    def GetAllOrders(self):
        r = self.session.get(self.base_endpoint+"getOrdersHistory")
        if r.status_code != 200:
            logger.error(
                f"Can't get orders history; Response: {r.text}, Status: {r.status_code}")
        return r.json()
        

    def getCatalog(self, group_id=None, with_image=False):
        try:
            r = self.session.get(self.base_endpoint+"getCatalog", params={
                "Image": 1 if with_image else 0,
                "ProductID": group_id
            }, timeout=REQUESTS_TIMEOUT*10 if group_id else 99999)

            if r.status_code != 200:
                logger.error(
                    f"Can't get catalog; Response: {r.text}, Status: {r.status_code}")
            if 'Ошибка' in r.text:
                logger.error(
                    f"Can't get catalog; Response: {r.text}, Status: {r.status_code}")
            data = r.json()

            data = [adaptGood(
                x, [y for y in data if y['ProductID'] == x['ProductID']]) for x in data]
            # Only qty in store
            data = [good for good in data if good['QtyInStore'] > 0]
            data = list({x['ProductID']: x for x in data}.values())
            
        except Exception as e:
            logger.error(f"Error get catalog: {e}")
            # Обработка ошибки таймаута
            data = [rdotdict(x) for x in MDB.Goods.find()]
        return data

    def getGood(self, good_id=None,  with_image=False):
        try:
            r = self.session.get(self.base_endpoint+"getCatalog", params={
                "Image": 1 if with_image else 0,
                "ProductID": good_id
            }, timeout=REQUESTS_TIMEOUT)
            if r.status_code != 200:
                logger.error(
                    f"Can't get catalog; Response: {r.text}, Status: {r.status_code}")
            result = r.json()
            if len(result) == 0:
                None

            good = adaptGood(result[0], result)
        except requests.exceptions.Timeout:
            logger.error("Time expired")
            # Обработка ошибки таймаута
            good = MDB.Goods.find_one(dict(ProductID=good_id))
            good = rdotdict(good) if good else None

        return good

    def getCatalogTree(self):
        try:

            r = self.session.get(self.base_endpoint + "getCatalogTree", timeout=REQUESTS_TIMEOUT)
            if r.status_code != 200:
                logger.error(
                    f"Can't get catalog; Response: {r.text}, Status: {r.status_code}")
            return r.json()
        except requests.exceptions.Timeout:
            logger.error("Time expired")
            # Обработка ошибки таймаута
            return list(MDB.Settings.find_one(dict(id="Catalog"))['catalog'].values())

    def getUsers(self):
        r = self.session.get(self.base_endpoint+"getUsers")
        if r.status_code != 200:
            logger.error(
                f"Can't get catalog; Response: {r.text}, Status: {r.status_code}")
        return r.json()
    
    def getUsersGroups(self):
        r = self.session.get(self.base_endpoint+"getUsersTree")
        if r.status_code != 200:
            logger.error(
                f"Can't get users groups; Response: {r.text}, Status: {r.status_code}")
        return r.json()

    def getUser(self, user_id):
        r = self.session.get(self.base_endpoint+"getUser",
                             params={"id": user_id})
        if r.status_code != 200:
            logger.error(
                f"Can't get catalog; Response: {r.text}, Status: {r.status_code}")
        return r.json()

    def getGoodImages(self, good_id):
        p = {
            "ProductID": good_id,
        }
        r = self.session.get(self.base_endpoint + "getProductImages", params=p)

        if r.status_code != 200:
            logger.error(
                f"Can't get images; Response: {r.text}, Status: {r.status_code}")
        images = []
        data = r.json()
        for x in data:
            if 'ProductImage' in x:
                images += [data[x]]
        logger.info(
            f"Get product images with sizes: {[len(x) for x in images]}")
        if images == [""]:
            return []
        return images
    
    def CreateOrder(self, user, storeID) -> bool:
        r = self.session.post(self.base_endpoint + "CreateOrder", timeout=REQUESTS_TIMEOUT,
                              json={
                                  "ClientID": user['diforce_data']['ID'],
                                  "StoreID": storeID,
                                  "Products": [
                                      {
                                          "ProductID": cartItem['ProductID'],
                                          "Quantity": cartItem['Quantity'],
                                          "Price": cartItem['Price'],
                                          "Sum": cartItem['Price'] * cartItem['Quantity']
                                      } for cartItem in list(user['cart'].values())
                                  ]
                              })
        if r.status_code != 200 or r.text == '':
            logger.error(
                f"Can't create order, error from 1c, response: {r.text}, Status: {r.status_code}")
            return None
        if 'MessageError' in r.json():
            logger.error(f"Can't create order, error from 1c: {r.json()['MessageError']}")
            return None
        return r.json()
            
    
    def GetUsersByParams(self, data):
        params =dict(
            FullName=data['full_name'],
        )
        if 'email' in data:
            params['Email'] = data['email']
        if 'phone' in data:
            params['Phone'] = data['phone']
        if 'inn+kpp' in data:
            params['INN'] = data['inn+kpp'].split('+')[0]
        if 'inn+kpp' in data and len(data['inn+kpp'].split('+')) > 1:
            params['KPP'] = data['inn+kpp'].split('+')[1]

        logger.info("-" * 20)
        logger.info(f"{data}{params}")
        params = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
        
        r = self.session.get(self.base_endpoint+"getUsersByParams", params=params,
                             timeout=REQUESTS_TIMEOUT)

        if r.status_code != 200:
            logger.error(
                f"Can't get catalog; Response: {r.text}, Status: {r.status_code}")
            
        rdata = r.json()
        return rdata
    
    def GetOrder(self, order_id, diforce_user_id):
        r = self.session.get(self.base_endpoint+"getOrder",
                             params={"OrderID": order_id,
                                     "ClientID":diforce_user_id})
        if r.status_code != 200:
            logger.error(
                f"Can't get catalog; Response: {r.text}, Status: {r.status_code}")
        return r.json()




OneService = OneServiceBase()
