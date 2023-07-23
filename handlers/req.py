
import copy
import datetime
import random
import traceback
from typing import Any, List, Union
from uuid import uuid4
import aiogram
from loggerConf import logger
import loguru
import pymongo
from etc.helpers import wrap_media
from etc.keyboards import Keyboards
from loader import MDB, dp, message_id_links, bot

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import  ChatTypeFilter
from aiogram.types import ChatType, CallbackQuery, ContentType, MediaGroup, InputFile, Message, InputMediaPhoto
from services.goodsService import GoodsService
from concurrent.futures import ThreadPoolExecutor

from services.oneService import OneService

import base64

from services.textService import Texts
from services.userService import UserService
from utils import prepareGoodItemToSend, process_string
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

MAX_IMAGES_IN_TELEGRAM_MEDIA_GROUP = 10
LEFT_STEP = 20
RIGHT_STEP = 20


def search_objects(objects_list, search_query):
    tokens_query = process_string(search_query)
    query_tokens_len = len(tokens_query)
    results = []
    for obj in objects_list:
        tokens_obj = process_string(f"{obj['Manufacturer']} {obj['ProductName']} {obj['ProductArt']}")
        score = 0
        if search_query.isdigit() and obj['ProductArt'].endswith(search_query) and len(search_query) >= 4:
            results.append((obj, score))
            continue
        for token in tokens_query:
            if token in tokens_obj:
                score += 1
        if score >= query_tokens_len:
            results.append((obj, score))
    r = sorted(results, key=lambda x: x[1], reverse=True)
            
    return [x[0] for x in r]


def apply_req(req: dict, user, exclude_filter=None):
    goods = list(MDB.Goods.find(dict(ProductID={"$in": req['GoodsIDs']}, QtyInStore={"$gt": 0})))
    if 'PriceFilter' in req['AppliedFilters'] and exclude_filter != 'PriceFilter':
        try:
            pr = 'Price' + user['opt']
        except Exception:
            pr = 'Price000000005'
        min_price = req['AppliedFilters']['PriceFilter']['min_price']
        max_price = req['AppliedFilters']['PriceFilter']['max_price']
        goods = [x for x in goods if min_price  <= x[pr] <= max_price]
        
    if 'BrandFilter' in req['AppliedFilters'] and exclude_filter != 'BrandFilter':
        brands = req['AppliedFilters']['BrandFilter']['Brands']
        goods = [x for x in goods if x['Manufacturer'] in brands]

    if 'QuerySearch' in req['AppliedFilters'] and exclude_filter != 'QuerySearch':
        search_query = req['AppliedFilters']['QuerySearch']
        goods = search_objects(goods, search_query)
    return goods

def get_category_tree(group, group_ids, catalog):
    """Функция для получения списка GroupID для всех категорий"""
    group_ids.append(group['GroupID'])
    if group['GroupID'] in catalog:
        subgroups = catalog[group['GroupID']]['Subgroups']
        for subgroup_id in subgroups:
            subgroup = subgroups[subgroup_id]
            # рекурсивно обходим дерево для каждой подкатегории
            get_category_tree(subgroup, group_ids, catalog)
    return group_ids


async def attach_photo(goodID, good_pic_messages: List[Message]):
    images = OneService.getGoodImages(goodID)
    

    # If has product image - send with image
    if images:
        true_images = []
        
        def process_image(image):
            b_img = base64.b64decode(image)
            try:
                img = Image.open(BytesIO(b_img))
            except UnidentifiedImageError:
                logger.error('Failed to identify the image')
                return None
            img_size = img.size
            if img_size[0] * img_size[1] > 160000:
                return wrap_media(b_img) # Возвращаем обернутое изображение, если размеры соответствуют условию
            else:
                return None # Возвращаем None, если размеры не соответствуют условию
            
        for img in images:
            last_processed_image = process_image(img)
            if last_processed_image:
                true_images += [last_processed_image]
                if len(true_images) >= 2:
                    break
        for good_pic_message in good_pic_messages:   
            if true_images:
                await good_pic_message.edit_media(true_images.pop())
            else:
                await good_pic_message.delete()

@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE), text_contains="|Catalog:", state="*")
async def _(c: CallbackQuery, state: FSMContext=None):
    stateData = await state.get_data() if state else {}
    action, *action_params = c.data.split(":")[1:]
    user = UserService.Get(c.from_user.id)
    
    if action == "root_categories":
        start_index = int(action_params[-1])
        categories = GoodsService.GetCategoriesTree()
        
        if start_index < 0:
            await c.answer("Вы в начале каталога")
            return
        if start_index > len(categories):
            await c.answer("Вы в конце каталога")
            return

        await c.message.edit_text(Texts.CatalogMessage, reply_markup=Keyboards.catalog(categories, user, start_index))
    
    if action in ["see_cat", "see_cat_goods"]:
        catID = action_params[0]
        categories = GoodsService.GetCategoriesTree()
        cat = GoodsService.GetCategoryByID(catID, categories)
        
        if catID == "":
            await c.message.edit_text(Texts.CatalogMessage, reply_markup=Keyboards.catalog(categories, user))
            return
        logger.info(f"See catalog for category {catID}")

        if cat == None:
            await c.message.answer(f"А вот оказывается тут баг и категории {catID} не существует")
            return

        goods = [x for x in list(MDB.Goods.find(dict(GroupID=cat['GroupID']))) if x['QtyInStore'] > 0]
        
        subcats_dfs = get_category_tree(cat, [], categories)
        extended_goods = [x for x in list(MDB.Goods.find()) if x['GroupID'] in subcats_dfs]
        req_id = None
        if extended_goods:
            req_id = str(uuid4())[:9]
            MDB.GoodsRequests.insert_one(dict(
                ID=req_id,
                GoodsIDs=[x['ProductID'] for x in extended_goods],
                CategoryID=catID,
                AppliedFilters={'GroupID': cat['GroupID']},
                CreatedAt=datetime.datetime.now()
            ))
            await state.update_data(req_id=req_id)

        if action == "see_cat" and list(cat['Subgroups'].values()):
            await c.message.edit_text(Texts.CategoryMessage.format(category=cat,
                                                                   subcategories_count=len(cat['Subgroups']),
                                                                   category_goods_count=len(goods)),
                                      reply_markup=Keyboards.category(cat, bool(goods)))
        elif goods:
            await c.message.edit_text(Texts.CategoryGoodsMessage.format(category=cat,
                                                                    goods_count=len(goods)),
                                  reply_markup=Keyboards.filteredGoods(cat, goods, req_id, head_cat=cat['HeadGroupID'] if not list(cat['Subgroups']) else cat['GroupID']))
        else:
            await c.answer("😶 В категории нет оптовых товаров!", show_alert=True)
    elif action == "see_good":
        goodID = action_params[0]
        good = GoodsService.GetGoodByID(goodID)
        good['Price'] = GoodsService.GetTargetPrice(user, good)
        good['ColorName'] = good['ColorName'].capitalize()
        
        messageText = prepareGoodItemToSend(good, user)
        
        logger.info(f"See good: {goodID}")
        await c.answer()
        sessionID = str(uuid4())[:9]
        keyboard = Keyboards.goodOptions(user, good, media_group_message_id=sessionID)
        
        # Ooooh fuck... saving in state message ids for goods to delete messages in future
        mg = MediaGroup()
        mg.attach_photo(InputFile("src/loading.png"))
        mg.attach_photo(InputFile("src/loading.png"))
        good_pic_messages: List[Message] = await c.message.answer_media_group(mg, disable_notification=True)
        good_message: Message = await c.message.answer(text=messageText, reply_markup=keyboard)
        
        good_pictures_msgs = (await state.get_data()).get('good_pictures_msgs', {})
        good_pictures_msgs[sessionID] = good_pic_messages + [good_message]
        await state.update_data(good_pictures_msgs=good_pictures_msgs)

        await attach_photo(goodID, good_pic_messages)
        
    elif action == "cancel_search":
        if state:
            await state.finish()
        await c.message.delete()
    elif action == "search":
        await c.answer()
        req_id = stateData.get('req_id', None)
        category_id = action_params[0]
        if '-' in category_id:
            req_id = category_id
            await state.update_data(req_id=req_id, category_id=None)
        else:
            category_id = category_id if category_id != "None" else None
            await state.update_data(category_id=category_id)

        msg = await c.message.answer(Texts.EnterSearchQuery, reply_markup=Keyboards.SearchQuery())
        await state.set_state("search")

        await state.update_data(msg_id=msg.message_id)

    elif action in ["price_filter", "brand_filter"]:
        category_group_id = action_params[0]
        if '-' in category_group_id:
            req_id = category_group_id
            await state.update_data(req_id=req_id, category_group_id=None)
        else:
            await state.update_data(category_group_id=category_group_id)

        if action == "price_filter":
            await c.message.answer(Texts.PriceFilterMessage, reply_markup=Keyboards.PriceFilterMessage())  
            await state.set_state("PriceFilterState")
        else:  # action == "brand_filter"
            req_id = stateData.get('req_id', None)
            
            if req_id is not None:
                req: Any = MDB.GoodsRequests.find_one(dict(ID=req_id))
                selected_brands = []
                if 'BrandFilter' in req['AppliedFilters']:
                    selected_brands = req['AppliedFilters']['BrandFilter']['Brands']
                all_brands = sorted(set(x['Manufacturer'] for x in apply_req(req, user, 'BrandFilter')))
            else:
                goods = list(MDB.Goods.find(dict(GroupID=category_group_id)))
                req = None
                all_brands = sorted(set(x['Manufacturer'] for x in goods))
                selected_brands = stateData.get("selected_brands", [])

            await c.message.answer(Texts.BrandFilterMessage, reply_markup=Keyboards.BrandFilter(all_brands, selected_brands, req))  
            await state.update_data(selected_brands=selected_brands, all_brands=all_brands, category_group_id=category_group_id)

        await c.answer()

    elif action == "brand_filter_choose":
        choosen_brand = action_params[0]
        selected_brands = stateData.get("selected_brands", [])
        if stateData.get("all_brands", []) != []:
            all_brands = sorted(stateData.get("all_brands", []))
        else: 
            all_brands = []
        req: Any = MDB.GoodsRequests.find_one(dict(ID=stateData.get('req_id', None)))

        if choosen_brand in selected_brands:
            selected_brands.remove(choosen_brand)
        else:
            selected_brands.append(choosen_brand)

        await c.message.edit_text(Texts.BrandFilterMessage, 
                                  reply_markup=Keyboards.BrandFilter(all_brands, selected_brands, req))  
        await state.update_data(selected_brands=selected_brands)
        await c.answer()

    elif action == "brand_filter_show":
        selected_brands = stateData.get("selected_brands", [])
        catID = stateData['category_group_id']

        logger.info(f"See catalog goods for category {catID}")

        categories = GoodsService.GetCategoriesTree()
        cat = GoodsService.GetCategoryByID(catID, categories)
        req_id = stateData.get('req_id', None)
        if req_id is None:
            subcats_dfs = get_category_tree(cat, [], categories)
            extended_goods = [x for x in list(MDB.Goods.find()) if x['GroupID'] in subcats_dfs]
            req_id = str(uuid4())[:9]
            req = dict(
                ID=req_id,
                GoodsIDs=[x['ProductID'] for x in extended_goods],
                CategoryID=catID,
                AppliedFilters={'BrandFilter': {"Brands": selected_brands}},
                CreatedAt=datetime.datetime.now()
            )
            MDB.GoodsRequests.insert_one(req)
            goods = apply_req(req, user)
        else:
            req: Any = MDB.GoodsRequests.find_one(dict(ID=stateData['req_id']))
            req['AppliedFilters']['BrandFilter'] = {"Brands": selected_brands}
            MDB.GoodsRequests.update_one(dict(ID=stateData['req_id']), {"$set": req})
            goods = apply_req(req, user)

        if not goods:
            await c.message.answer(Texts.NoGoodsForFilter, reply_markup=Keyboards.backToCategory(cat))
            return
        
        try:
            await c.message.answer(Texts.BrandsGoodsMessage.format(goods_count=len(goods)),
                                    reply_markup=Keyboards.filteredGoods(cat, goods, req_id))
        except aiogram.utils.exceptions.BadRequest as e:
            logger.error(f"{e}; {traceback.format_exc()}")
            await c.message.answer(Texts.TooManyGoodsException)

    elif action == "cancel_filter":
        req: Any = MDB.GoodsRequests.find_one(dict(ID=stateData.get('req_id', None)))
        if req:
            MDB.GoodsRequests.update_one(dict(ID=req['ID']), {"$set": {"AppliedFilters": {}}})
        await c.answer()
        await c.message.delete()

    elif action == "main":
        categories = GoodsService.GetCategoriesTree()
        await c.message.edit_text(Texts.CatalogMessage, reply_markup=Keyboards.catalog(categories, user))


@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE), text_contains="|FilteredGoods:", state="*")
async def _(c: CallbackQuery, state: FSMContext):
    if state:
        await state.finish()
    mode, req_id, start_index = c.data.split(":")[1:4]
    start_index = int(start_index)

    user = UserService.Get(c.from_user.id)
    req: Any = MDB.GoodsRequests.find_one(dict(ID=req_id))
    categories = GoodsService.GetCategoriesTree()
    category = GoodsService.GetCategoryByID(req['CategoryID'], categories)
    goods = list(MDB.Goods.find(dict(ProductID={"$in": req['GoodsIDs']}, QtyInStore={"$gt": 0})))
    goods = apply_req(req, user)

    if mode == "left":
        start_index = max(0, start_index - 20)
    if mode == "right":
        start_index = min(len(req['GoodsIDs']), start_index + 20)

    try:
        await c.message.edit_reply_markup(reply_markup=Keyboards.filteredGoods(category, goods, req_id, start_index))
    except aiogram.utils.exceptions.BadRequest as e:
        logger.error(f"{e}; {traceback.format_exc()}")
        await c.message.answer(Texts.TooManyGoodsException)
