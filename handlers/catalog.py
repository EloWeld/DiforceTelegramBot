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
    if state:
        await state.finish()
    action = c.data.split(":")[1]
    user = UserService.Get(c)

    if action == "add_to_cart":
        await c.answer()
        goodID = c.data.split(":")[2]
        good = GoodsService.GetGoodByID(goodID)
        UserService.AddToCart(user.id, good)
        await c.message.answer(Texts.AddedToCart, reply_markup=Keyboards.startMenu(user))

    if action == "found_cheaper":
        await c.answer()
        goodID = c.data.split(":")[2]
        await state.set_state("FoundItCheaper")
        ans_msg = await c.message.answer(Texts.FoundCheaperMessage, reply_markup=Keyboards.foundCheaperMenu())
        await state.update_data(goodID=goodID, msgID=ans_msg.message_id)

    if action == "store_quants":
        await c.answer()
        goodID = c.data.split(":")[2]
        store_text = '\n'.join(Texts.QuantityInStoresFormat.format(
            **x) for x in GoodsService.GetGoodByID(goodID)['QuantityInStores'])
        await c.message.answer(Texts.QuantityInStores.format(store_text=store_text), reply_markup=Keyboards.storeQuantsKb())

    if action == "hide":
        await c.answer()
        mid = c.data.split(":")[2]
        if mid != "None" and mid in message_id_links:
            for x in message_id_links[mid]:
                try:
                    await bot.delete_message(c.message.chat.id, int(x))
                except Exception as e:
                    pass
        await c.message.delete()


@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE), text_contains="|Catalog:", state="*")
async def _(c: CallbackQuery, state: FSMContext):
    if state:
        await state.finish()
    action = c.data.split(":")[1]
    user = UserService.Get(c.from_user.id)
    
    if action == "see_cat":
        catID = c.data.split(":")[2]
        loguru.logger.info(f"See catalog for category {catID}")

        cat = GoodsService.GetCategoryByID(catID)
        if cat == None:
            await c.message.answer(f"А вот оказывается тут баг и категории {catID} не существует")
            return
        subcategories_count = len(cat['Subgroups'])
        goods = list(MDB.Goods.find(dict(GroupID=cat['GroupID'])))
        category_goods_count = len(goods)

        # If category contains subcategories - throw another keyboard
        if subcategories_count == 0:
            await c.message.edit_text(Texts.CategoryGoodsMessage.format(category=cat,
                                                                        goods_count=len(goods)),
                                      reply_markup=Keyboards.categoryGoods(cat, goods[:30], head_cat=cat['HeadGroupID']))
        else:
            await c.message.edit_text(Texts.CategoryMessage.format(category=cat,
                                                                   subcategories_count=subcategories_count,
                                                                   category_goods_count=category_goods_count),
                                      reply_markup=Keyboards.category(cat, goods != []))

    if action == "see_cat_goods":
        catID = c.data.split(":")[2]

        loguru.logger.info(f"See catalog goods for category {catID}")

        cat = GoodsService.GetCategoryByID(catID)
        goods = list(MDB.Goods.find(dict(GroupID=cat['GroupID'])))
        category_goods_count = len(goods)
        req_id = str(uuid4())[:6]
        MDB.GoodsRequests.insert_one(dict(
            ID=req_id,
            GoodsIDs=[x['ProductID'] for x in goods],
            CategoryID=catID,
            CreatedAt=datetime.datetime.now()
        ))

        try:
            await c.message.edit_text(Texts.CategoryGoodsMessage.format(category=cat,
                                                                    goods_count=len(goods)),
                                  reply_markup=Keyboards.filteredGoods(cat, goods, req_id, head_cat=cat['GroupID']))
        except aiogram.utils.exceptions.BadRequest as e:
            await c.answer(Texts.TooManyGoodsException)
    if action == "see_good":
        goodID = c.data.split(":")[2]
        good, images = GoodsService.GetGoodByID(goodID, with_images=True)
        good['Price'] = GoodsService.GetTargetPrice(user, good)
        good['ColorName'] = good['ColorName'].capitalize()
        good['Price'] = f"{good['Price']:,}".replace(',',' ')
        messageText = Texts.GoodCard.format(**good)
        
        loguru.logger.info(f"See good: {goodID}")

        # If has product image - send with image
        if images != []:
            from PIL import Image
            from io import BytesIO

            images = list(set(images))
            # Build media group
            attached_images_count = 0
            media_group = MediaGroup()
            for i in range(10): # 10 - maximum images in telegram media group
                b_img = base64.b64decode(images[i])
                img_size = Image.open(BytesIO(b_img)).size
                print('Image size:', img_size)
                # Check that image not too small
                if img_size[0]*img_size[1] > 160000:
                    attached_images_count += 1
                    media_group.attach_photo(wrap_media(b_img))
                if len(images) == i + 1: # if we walk around all images
                    break
                
            # Send media group and message
            mid = await c.message.answer_media_group(media_group)
            message_id_links[str(mid[0].message_id)] = [x.message_id for x in mid]
            keyboard = Keyboards.goodOptions(good, mid[0].message_id)
            await c.message.answer(messageText, reply_markup=keyboard)
        else:
            keyboard = Keyboards.goodOptions(good)
            await c.message.answer(messageText, reply_markup=keyboard)

    if action == "cancel_search":
        if state:
            await state.finish()
        await c.message.delete()
        
    if action == "search":
        category_id = c.data.split(':')[2]
        category_id = category_id if category_id != "None" else None
        msg = await c.message.answer(Texts.EnterSearchQuery, reply_markup=Keyboards.SearchQuery())
        await state.set_state("search")
        await state.update_data(category_id=category_id, msg_id=msg.message_id)
        
    if action == "price_filter": 
        category_group_id = goodID = c.data.split(":")[2]
        await c.message.answer(Texts.PriceFilterMessage, reply_markup=Keyboards.PriceFilterMessage())  
        await state.set_state("PriceFilterState")
        await state.update_data(category_group_id=category_group_id)
        await c.answer()
    if action == "cancel_filter":
        await state.finish()
        await c.answer()
        await c.message.delete()
    if action == "main":
        categories = GoodsService.GetCategoriesTree()

        await c.message.edit_text(Texts.CatalogMessage, reply_markup=Keyboards.catalog(categories))

@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE), text_contains="|FilteredGoods:", state="*")
async def _(c: CallbackQuery, state: FSMContext):
    if state:
        await state.finish()
    mode = c.data.split(":")[1]
    req_id = c.data.split(":")[2]
    start_index = int(c.data.split(":")[3])
    user = UserService.Get(c.from_user.id)
    r = MDB.GoodsRequests.find_one(dict(ID=req_id))
    cat = GoodsService.GetCategoryByID(r['CategoryID'])
    goods = [MDB.Goods.find_one(dict(ProductID=x)) for x in r['GoodsIDs']]
    if mode == "left":
        start_index = max(0, start_index - 20)
    if mode == "right":
        start_index = min(len(r['GoodsIDs']), start_index + 20)
    try:
        await c.message.edit_reply_markup(reply_markup=Keyboards.filteredGoods(cat, goods, req_id, start_index))
    except aiogram.utils.exceptions.BadRequest as e:
        loguru.logger.error(f"{e}; {traceback.format_exc()}")
        await c.message.answer(Texts.TooManyGoodsException)

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
    catID = stateData['category_group_id']

    loguru.logger.info(f"See catalog goods for category {catID}")

    cat = GoodsService.GetCategoryByID(catID)
    goods = list(MDB.Goods.find(dict(GroupID=cat['GroupID'])))
    pr = 'PriceOptSmall' if user['opt'] == "SmallOpt" else 'PriceOptMiddle' if user['opt'] == "MiddleOpt" else 'PriceOptLarge' if user['opt'] == "LargeOpt" else 'Price'
    goods = [x for x in goods if min_price <= x[pr] <= max_price]
    req_id = str(uuid4())[:6]
    MDB.GoodsRequests.insert_one(dict(
        ID=req_id,
        GoodsIDs=[x['ProductID'] for x in goods],
        CategoryID=catID
    ))

    if goods == []:
        await m.answer(Texts.NoGoodsForFilter, reply_markup=Keyboards.backToCategory(cat))
        return
    
    try:
        await m.answer(Texts.CategoryGoodsMessage.format(category=cat, goods_count=len(goods)),
                                reply_markup=Keyboards.filteredGoods(cat, goods, req_id))
    except aiogram.utils.exceptions.BadRequest as e:
        loguru.logger.error(f"{e}; {traceback.format_exc()}")
        await m.answer(Texts.TooManyGoodsException)
    
    
    
@dp.message_handler(state="search")
async def _(m: Message, state: FSMContext):
    stateData = await state.get_data()
    user = UserService.Get(m.from_user.id)
    
    search_query = m.text
    cat_id=stateData.get("category_id")
    
    await state.finish()
    
    cond = {}
    if cat_id:
        cond = dict(GroupID=cat_id)
    goods = sorted(MDB.Goods.find(cond), key=lambda x: (
        fuzz.partial_ratio(m.text.lower(), x['ProductName'].lower())
    ), reverse=True)
    
    cat = GoodsService.GetCategoryByID(cat_id)
    # Cut goods to maximum 30 probability
    for i in range(len(goods)):
        probability = fuzz.partial_ratio(m.text.lower(), goods[i]['ProductName'].lower())
        print(probability, goods[i]['ProductName'])
        if probability < 50:
            goods = [rdotdict(x) for x in goods[:i]]
            break
    req_id = str(uuid4())[:6]
    MDB.GoodsRequests.insert_one(dict(
        ID=req_id,
        GoodsIDs=[x['ProductID'] for x in goods],
        CategoryID=cat_id
    ))
    await m.answer(Texts.SearchResults.format(found_count=len(goods)), reply_markup=Keyboards.filteredGoods(cat, goods, req_id))
    
    try:
        await bot.delete_message(m.chat.id, stateData.get('msg_id'))
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
