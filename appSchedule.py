import asyncio
from threading import Thread
import time
import traceback
import loguru
from loader import MDB, bot
from dotdict import dotdict
import schedule

from services.oneService import OneService

FORBIDDEN_GROUP_IDS = [
    "ЦБ000000011",
    "ЦБ000000017",
    "ЦБ000000018",
    "ЦБ000000091"
    "DI000001303",
    "DI000002842",
    "DI000003552",
    "DI000004090",
    "00000000001",
    "DI000004809",
    "DI000007050",
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
    loguru.logger.info(f"[CATALOG]: Start sync tree")
    startTime = time.time()
    data = OneService.getCatalogTree()
    data.sort(key=lambda x: x['HeadGroupID'])
    catalog = {}
    fillCatalog(catalog, data, '')
    catalog = {k: v for k, v in sorted(
        catalog.items(), key=lambda item: item[1]['GroupName'])}

    if not MDB.Settings.find_one(dict(id="Catalog")):
        MDB.Settings.insert_one(dict(id="Catalog"))
    MDB.Settings.update_one(dict(id="Catalog"), {
                            "$set": dict(catalog=catalog)})
    loguru.logger.success(f"[CATALOG]: Catalogs tree has been updated successfully within {time.time() - startTime} seconds")


async def catalogGoodsSync():
    loguru.logger.info(f"[CATALOG]: Start sync catalog")
    startTime = time.time()
    data = OneService.getCatalog(with_image=False)
    MDB.Goods.delete_many({})
    loguru.logger.info(f"[CATALOG]: All goods was deleted")
    for x in data:
        MDB.Goods.insert_one(x)
    loguru.logger.success(f"[CATALOG]: Catalogs has been updated successfully within {time.time() - startTime} seconds")

async def diforceUsersSync():
    loguru.logger.info("[DIFORCE-USERS]: Start sync users")
    try:
        users = OneService.getUsers()
        MDB.DiforceUsers.delete_many({})
        for x in users:
            MDB.DiforceUsers.insert_one(x)
    except Exception as e:
        loguru.logger.error(f"[DIFORCE-USERS]: Can't sync diforce users!: {e}; traceback: {traceback.format_exc()}")
    loguru.logger.info(f"[CATALOG]: Users synced")
    
    
def diforceUsersSyncWrapper():
    while True:
        asyncio.run(diforceUsersSync())
        time.sleep(2000)
        

th1 = Thread(target=diforceUsersSyncWrapper, name="Sync users from diforce thread")
th1.start()
schedule.every(2).minutes.at(":37").do(lambda: asyncio.run(catalogTreeSync()))
schedule.every(10).minutes.at(":37").do(lambda: asyncio.run(catalogGoodsSync()))

loguru.logger.info("Starting scheduler")

asyncio.run(catalogTreeSync())
asyncio.run(catalogGoodsSync())


while True:
    schedule.run_pending()
    time.sleep(1)
