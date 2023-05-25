from concurrent.futures import ThreadPoolExecutor
import datetime
import traceback
from uuid import uuid4
import aiogram
import loguru
from etc.filters import AntiSpam
from etc.helpers import rdotdict, wrap_media
from etc.keyboards import Keyboards
from handlers.req import apply_req, get_category_tree
from loader import MDB, dp, bot, Consts, message_id_links
from io import BytesIO
from PIL import Image
from fuzzywuzzy import fuzz

from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text, ChatTypeFilter
from aiogram.types import Message, ChatType
from services.goodsService import GoodsService

from services.oneService import OneService

import base64
from dotdict import dotdict

from services.textService import Texts
from services.userService import UserService


# ▒▄█▀▀█░▐█▀▀─░▄█▀▄─▒▐█▀▀▄░▐█▀█░▐█░▐█
# ▒▀▀█▄▄░▐█▀▀░▐█▄▄▐█▒▐█▒▐█░▐█──░▐████
# ▒█▄▄█▀░▐█▄▄░▐█─░▐█▒▐█▀▄▄░▐█▄█░▐█░▐█



# ░▐█▀█─░▄█▀▄─▒█▀█▀█─░▄█▀▄─▒██░░░▒▐█▀▀█▌░▐█▀▀▀─
# ░▐█──░▐█▄▄▐█░░▒█░░░▐█▄▄▐█▒██░░░▒▐█▄▒█▌░▐█░▀█▌
# ░▐█▄█░▐█─░▐█░▒▄█▄░░▐█─░▐█▒██▄▄█▒▐██▄█▌░▐██▄█▌


@dp.message_handler(Text(Texts.CatalogButton), AntiSpam(), ChatTypeFilter(ChatType.PRIVATE), state="*")
async def _(m: Message, state: FSMContext):
    if state:
        await state.finish()
    categories = GoodsService.GetCategoriesTree()

    await m.answer(Texts.CatalogMessage, reply_markup=Keyboards.catalog(categories))


@dp.message_handler(state="PriceFilterState")
async def _(m: Message, state: FSMContext):
    stateData = await state.get_data()
    user = UserService.Get(m.from_user.id)
    
    try:
        min_price = float(m.text.replace('-', ' ').split(' ')[0])
        max_price = float(m.text.replace('-', ' ').split(' ')[1])
        await state.update_data(min_price=min_price, max_price=max_price)
        await m.answer(Texts.RangeSetted)
    except Exception as e:
        await m.answer(Texts.InvalidRange)
        loguru.logger.error(f"Invalid range or idk: error {e}")
        return
    # See goods
    catID = stateData.get('category_group_id', None)

    loguru.logger.info(f"See catalog goods for category {catID}")

    categories = GoodsService.GetCategoriesTree()
    cat = GoodsService.GetCategoryByID(catID, categories)
    
    req_id = stateData.get('req_id', None)
    if req_id:
        req = MDB.GoodsRequests.find_one(dict(ID=req_id))
        req['AppliedFilters']['PriceFilter'] = {'min_price': min_price, 'max_price': max_price}
        goods = apply_req(req, user)
        MDB.GoodsRequests.update_one(dict(ID=req_id), {"$set": req})
    else:
        subcats_dfs = get_category_tree(cat, [], categories)
        extended_goods = [x for x in list(MDB.Goods.find()) if x['GroupID'] in subcats_dfs]
        req_id = str(uuid4())[:9]
        req = dict(
            ID=req_id,
            GoodsIDs=[x['ProductID'] for x in extended_goods],
            CategoryID=catID,
            AppliedFilters={'PriceFilter':{'min_price': min_price, 'max_price': max_price}},
            CreatedAt=datetime.datetime.now()
        )
        MDB.GoodsRequests.insert_one(req)
        goods = apply_req(req, user)

    if goods == []:
        await m.answer(Texts.NoGoodsForFilter, reply_markup=Keyboards.backToCategory(cat))
        return
    
    try:
        await m.answer(Texts.FilteredGoodsMessage + f" ({len(goods)})",
                                reply_markup=Keyboards.filteredGoods(cat, goods, req_id))
    except aiogram.utils.exceptions.BadRequest as e:
        loguru.logger.error(f"{e}; {traceback.format_exc()}")
        await m.answer(Texts.TooManyGoodsException)
    
    
@dp.message_handler(state="search")
async def search_handler(m: Message, state: FSMContext):
    state_data = await state.get_data()
    user = UserService.Get(m.from_user.id)
    
    search_query = m.text
    cat_id = state_data.get("category_id")
    cat = None
    
    req_id = state_data.get('req_id')
    if req_id is not None:
        req = MDB.GoodsRequests.find_one(dict(ID=state_data['req_id']))
        req['AppliedFilters']['QuerySearch'] = search_query
        goods = apply_req(req, user)
        MDB.GoodsRequests.update_one({"ID": req['ID']}, {"$set": req})
    else:
        categories = GoodsService.GetCategoriesTree()
        cat = GoodsService.GetCategoryByID(cat_id, categories)
        req_id = str(uuid4())[:9]
        req = {
            "ID": req_id, "GoodsIDs": [x['ProductID'] for x in MDB.Goods.find(dict(), {"ProductID": 1})],
            "CategoryID": cat_id,
            "AppliedFilters": {'QuerySearch': search_query},
            "CreatedAt": datetime.datetime.now()}
        MDB.GoodsRequests.insert_one(req)
        goods = apply_req(req, user)
    
    await state.update_data(req_id=req_id)
    await m.answer(Texts.SearchResults.format(found_count=len(goods)), reply_markup=Keyboards.filteredGoods(cat, goods, req_id))
    
    try:
        await bot.delete_message(m.chat.id, state_data.get('msg_id'))
    except Exception as e:
        loguru.logger.error(f"Can't delete message: {e}")
