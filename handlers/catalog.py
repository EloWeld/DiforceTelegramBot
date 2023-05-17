import datetime
import traceback
from uuid import uuid4
import aiogram
import loguru
from etc.filters import AntiSpam
from etc.helpers import rdotdict, wrap_media
from etc.keyboards import Keyboards
from loader import MDB, dp, bot, Consts, message_id_links
from io import BytesIO

from fuzzywuzzy import fuzz

from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text, ChatTypeFilter
from aiogram.types import Message, ChatType, BotCommand, CallbackQuery, ContentType, MediaGroup, InputFile
from services.goodsService import GoodsService

from services.oneService import OneService

import base64
from dotdict import dotdict

from services.textService import Texts
from services.userService import UserService
from utils import prepareGoodItemToSend


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


@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE), text_contains="|Good:", state="*")
async def _(c: CallbackQuery, state: FSMContext):
    global message_id_links
    action = c.data.split(":")[1]
    user = UserService.Get(c)

    if action == "add_to_cart":
        await c.answer()
        goodID = c.data.split(":")[2]
        good = GoodsService.GetGoodByID(goodID)
        if good['QtyInStore'] == 0:
            await c.message.answer("❌ Товара нет на складе, добавить в корзину невозможно")
            return
        UserService.AddToCart(user.id, good)
        await c.message.answer(Texts.AddedToCart, reply_markup=Keyboards.addedToCart(good))

    if action == "found_cheaper":
        await c.answer()
        goodID = c.data.split(":")[2]
        await state.set_state("FoundItCheaper")
        ans_msg = await c.message.answer(Texts.FoundCheaperMessage, reply_markup=Keyboards.foundCheaperMenu())
        await state.update_data(goodID=goodID, msgID=ans_msg.message_id)

    if action == "hide":
        await c.answer()
        mid = c.data.split(":")[2]
        good_pictures_msgs = (await state.get_data()).get('good_pictures_msgs', {})
        if mid in good_pictures_msgs:
            for good_msg in good_pictures_msgs[mid]:
                try:
                    await good_msg.delete()
                except Exception as e:
                    pass
        await c.message.delete()
        
        if state:
            await state.finish()
    


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

    cat = GoodsService.GetCategoryByID(catID)
    
    req_id = stateData.get('req_id', None)
    if req_id:
        req = MDB.GoodsRequests.find_one(dict(ID=req_id))
        goods = list(MDB.Goods.find(dict(ProductID={"$in":req['GoodsIDs']})))
    else:
        goods = list(MDB.Goods.find(dict(GroupID=cat['GroupID'])))
    
    pr = 'PriceOptSmall' if user['opt'] == "SmallOpt" else 'PriceOptMiddle' if user['opt'] == "MiddleOpt" else 'PriceOptLarge' if user['opt'] == "LargeOpt" else 'Price'
    goods = [x for x in goods if min_price <= x[pr] <= max_price and x['QtyInStore'] > 0]
    
    if req_id:
        req['GoodsIDs'] = [x['ProductID'] for x in goods]
        req['AppliedFilters']['PriceFilter'] = {'min_price': min_price, 'max_price': max_price}
        MDB.GoodsRequests.update_one(dict(ID=req_id), {"$set": req})
    else:
        req_id = str(uuid4())[:9]
        MDB.GoodsRequests.insert_one(dict(
            ID=req_id,
            GoodsIDs=[x['ProductID'] for x in goods],
            CategoryID=catID,
            AppliedFilters={'PriceFilter':{'min_price': min_price, 'max_price': max_price}},
            CreatedAt=datetime.datetime.now()
        ))

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
    
    goods = MDB.Goods.find(
        {"$text": {"$search": search_query}},
        {"score": {"$meta": "textScore"}}
    ).sort([("score", {"$meta": "textScore"})])
    
    goods = [x for x in goods if x['QtyInStore'] > 0]
    
    req_id = state_data.get('req_id')
    if req_id is not None:
        req = MDB.GoodsRequests.find_one({"ID": state_data['req_id']})
        goods = [x for x in goods if x['ProductID'] in req['GoodsIDs']]
        req['GoodsIDs'] = [x['ProductID'] for x in goods]
        req['AppliedFilters']['QuerySearch'] = search_query
        MDB.GoodsRequests.update_one({"ID": req['ID']}, {"$set": req})
    else:
        cat = GoodsService.GetCategoryByID(cat_id)
        req_id = str(uuid4())[:9]
        MDB.GoodsRequests.insert_one({
            "ID": req_id,
            "GoodsIDs": [x['ProductID'] for x in goods],
            "CategoryID": cat_id,
            "AppliedFilters": {'QuerySearch': search_query},
            "CreatedAt": datetime.datetime.now()
        })
    
    await state.update_data(req_id=req_id)
    await m.answer(Texts.SearchResults.format(found_count=len(goods)), reply_markup=Keyboards.filteredGoods(cat, goods, req_id))
    
    try:
        await bot.delete_message(m.chat.id, state_data.get('msg_id'))
    except Exception as e:
        loguru.logger.error(f"Can't delete message: {e}")

# =============== FOUND CHEAPER ===============

@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE), content_types=[ContentType.TEXT, ContentType.PHOTO], state="FoundItCheaper")
async def _(m: Message, state: FSMContext):
    stateData = dotdict(await state.get_data())
    user = UserService.Get(m.from_user.id)
    await state.finish()
    if m.text == Texts.QuitButton:
        await m.answer('👌🏻', reply_markup=Keyboards.startMenu(user))
        await m.delete()
        await bot.delete_message(m.chat.id, stateData.msgID)
        return
    good = GoodsService.GetGoodByID(stateData.goodID)
    comment = m.text if m.text else m.caption if m.caption else '➖'
    # Define admin type for send message
    if 'SmallOpt' in user.roles or 'MiddleOpt' in user.roles or 'LargeOpt' in user.roles:
        contact = Consts.OptContactTGID
    else:
        contact = Consts.RetailContactTGID

    # Build text
    messageText = Texts.FoundCheaperAdminMessage.format(
        good=good, user=user, comment=comment, BotUsername=Consts.BotUsername)

    # If has attached photo - send photo
    if len(m.photo) > 0:
        await bot.send_photo(contact, caption=messageText, photo=m.photo[0].file_id)
    else:
        await bot.send_message(contact, text=messageText)
    await m.answer(Texts.YourRequestWasSentMessage, reply_markup=Keyboards.startMenu(user))
