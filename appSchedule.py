import asyncio
import datetime
from threading import Thread
import time
import traceback
import loguru
from loader import MDB, bot
from dotdict import dotdict
import schedule
from loggerConf import logger
from services.oneService import OneService
from utils import format_phone_number, is_in_group_hierarchy

FORBIDDEN_GROUP_IDS = [
    "00000000001", # 1Прочее
    "ЦБ000000011", # ОЖИДАЮТСЯ НОВИНКИ
    "ЦБ000000017", # БОЛЬШЕ НЕ БУДЕТ ПОСТУПЛЕНИЯ (АРХИВ)
    "ЦБ000000018", # Сертификаты
    "ЦБ000000091" # Товары под заказ
    "DI000001303", # Выстовочные стенды
    "DI000002842", # Услуги
    "DI000003552", # Для печати фотографий
    "DI000004090", # УЦЕНКА
    "DI000004809", # ТОВАР НА МИРА 60
    "DI000007050", # Всё для зарядки
]

ALLOWED_USER_GROUPS = [
    "DI0000764", # КРУПНЫЙ ОПТ
    "ЦБ0000028", # ПОКУПАТЕЛИ ОПТОВЫЕ
    "ЦБ0000540", # РОЗНИЧНЫЕ ПОКУПКИ
    "ИН0000002", # СОТРУДНИКИ
    "ИН0000035", # ООО НКО Яндекс Директ
    "000000018", # Частное лицо (возврат)
    "DI0000527", # СПЕЦ ЦЕНА ОПТ
    
    "ЦБ0000021", # НАШИ МАГАЗИНЫ
]


def fillCatalog(catalog, data, head):
    for xCategory in data:
        if xCategory['GroupID'] in FORBIDDEN_GROUP_IDS:
            continue
        if xCategory['HeadGroupID'] == head:
            catalog[xCategory['GroupID']] = xCategory
            xCategory['Subgroups'] = {}
            fillCatalog(xCategory['Subgroups'], data, xCategory['GroupID'])


async def catalogTreeSync():
    logger.info(f"[CATALOG]: Start sync tree")
    startTime = time.time()
    saved_catalog = MDB.Settings.find_one(dict(id="Catalog"))
    last_saved_order = 0
    data = OneService.getCatalogTree()
    for x in data:
        if saved_catalog and x['GroupID'] in saved_catalog['catalog'] and 'order' in saved_catalog['catalog'][x['GroupID']]:
            x['order'] = saved_catalog['catalog'][x['GroupID']]['order']
        else:
            x['order'] = last_saved_order
            last_saved_order += 1
    data.sort(key=lambda x: x['HeadGroupID'])
    catalog = {}
    fillCatalog(catalog, data, '')
    catalog = {k: v for k, v in sorted(
        catalog.items(), key=lambda item: item[1]['GroupName'])}

    if not MDB.Settings.find_one(dict(id="Catalog")):
        MDB.Settings.insert_one(dict(id="Catalog"))
    MDB.Settings.update_one(dict(id="Catalog"), {
                            "$set": dict(catalog=catalog)})
    logger.debug(
        f"[CATALOG]: Catalogs tree has been updated successfully within {time.time() - startTime} seconds")


async def catalogGoodsSync():
    logger.info(f"[CATALOG]: Start sync catalog")
    startTime = time.time()
    data = OneService.getCatalog(with_image=False)
    MDB.Goods.delete_many({})
    logger.info(f"[CATALOG]: All goods was deleted")
    for x in data:
        MDB.Goods.insert_one(x)
    logger.debug(
        f"[CATALOG]: Catalogs has been updated successfully within {time.time() - startTime} seconds")


async def goodRequestsCleaner():
    MDB.GoodsRequests.delete_many(
        dict(CreatedAt={"$lt": datetime.datetime.now() - datetime.timedelta(days=1)}))

async def diforceUsersSync():
    logger.info("[DIFORCE-USERS]: Start sync users")
    contractTypes = {}
    try:
        users = OneService.getUsers()
        user_groups = OneService.getUsersGroups()
        filtered_users = []
        excluded_user_groups = set()
        # Change users objects
        for x_user in users:
            if x_user['Phone']:
                x_user['Phone'] = format_phone_number(x_user['Phone'])
            if is_in_group_hierarchy(x_user['GroupID'], ALLOWED_USER_GROUPS, user_groups):
                filtered_users.append(x_user)
                contractTypes[x_user['ContractTypeCode']] = x_user['ContractType']
            else:
                g = [x for x in user_groups if x['GroupID'] == x_user['GroupID']]
                excluded_user_groups.add(g[0]['GroupName'] if g else '???')
                
        logger.info(excluded_user_groups)
        MDB.DiforceUsers.delete_many({})
        MDB.DiforceUsers.insert_many(filtered_users)
        MDB.Settings.update_one(dict(id="Constants"), {"$set": dict(ContractTypes=contractTypes)})
    except Exception as e:
        logger.error(
            f"[DIFORCE-USERS]: Can't sync diforce users!: {e}; traceback: {traceback.format_exc()}")
    logger.info(f"[CATALOG]: Users synced")

async def clearLogs():
    with open('botlog_debug.log','w') as f:
        f.write('')
    with open('botlog_info.log','w') as f:
        f.write('')
    with open('botlog_warning.log','w') as f:
        f.write('')
    with open('botlog_error.log','w') as f:
        f.write('')
    with open('ServiceErrors.log','w') as f:
        f.write('')
    with open('ServiceOutput.log','w') as f:
        f.write('')
    print("Logs clerared")

def diforceUsersSyncWrapper():
    while True:
        asyncio.run(diforceUsersSync())
        time.sleep(2000)


th1 = Thread(target=diforceUsersSyncWrapper,
             name="Sync users from diforce thread")
th1.start()
schedule.every(2).minutes.at(":00").do(lambda: asyncio.run(catalogTreeSync()))
schedule.every(3).minutes.at(":00").do(lambda: asyncio.run(catalogGoodsSync()))
schedule.every(12).hours.at(":00").do(lambda: asyncio.run(clearLogs()))
schedule.every(50).minutes.at(":00").do(
    lambda: asyncio.run(goodRequestsCleaner()))

logger.info("Starting scheduler")
asyncio.run(clearLogs())
asyncio.run(goodRequestsCleaner())
asyncio.run(catalogTreeSync())
asyncio.run(catalogGoodsSync())


while True:
    try:
        schedule.run_pending()
    except Exception as e:
        logger.error(e)
        
    time.sleep(1)
