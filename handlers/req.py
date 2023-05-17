
import datetime
import random
import traceback
from uuid import uuid4
import aiogram
import loguru
from etc.helpers import wrap_media
from etc.keyboards import Keyboards
from loader import MDB, dp, message_id_links

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import  ChatTypeFilter
from aiogram.types import ChatType, CallbackQuery, ContentType, MediaGroup, InputFile
from services.goodsService import GoodsService
from concurrent.futures import ThreadPoolExecutor

from services.oneService import OneService

import base64

from services.textService import Texts
from services.userService import UserService
from utils import prepareGoodItemToSend
from PIL import Image
from io import BytesIO

MAX_IMAGES_IN_TELEGRAM_MEDIA_GROUP = 10
LEFT_STEP = 20
RIGHT_STEP = 20

@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE), text_contains="|Catalog:", state="*")
async def _(c: CallbackQuery, state: FSMContext=None):
    stateData = await state.get_data() if state else {}
    action, *action_params = c.data.split(":")[1:]
    user = UserService.Get(c.from_user.id)
    
    if action in ["see_cat", "see_cat_goods"]:
        catID = action_params[0]
        if catID == "":
            categories = GoodsService.GetCategoriesTree()
            await c.message.edit_text(Texts.CatalogMessage, reply_markup=Keyboards.catalog(categories))
            return
        loguru.logger.info(f"See catalog for category {catID}")

        cat = GoodsService.GetCategoryByID(catID)
        if cat == None:
            await c.message.answer(f"А вот оказывается тут баг и категории {catID} не существует")
            return

        goods = [x for x in list(MDB.Goods.find(dict(GroupID=cat['GroupID']))) if x['QtyInStore'] > 0]
        if goods:
            req_id = str(uuid4())[:9]
            MDB.GoodsRequests.insert_one(dict(
                ID=req_id,
                GoodsIDs=[x['ProductID'] for x in goods],
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
        good, images = GoodsService.GetGoodByID(goodID, with_images=True)
        good['Price'] = GoodsService.GetTargetPrice(user, good)
        good['ColorName'] = good['ColorName'].capitalize()
        
        messageText = prepareGoodItemToSend(good)
        
        loguru.logger.info(f"See good: {goodID}")
        
        # If has product image - send with image
        if images:
            media_group = MediaGroup()
            
            def process_image(image):
                b_img = base64.b64decode(image)
                img = Image.open(BytesIO(b_img))
                img_size = img.size
                if img_size[0] * img_size[1] > 160000:
                    return wrap_media(b_img) # Возвращаем обернутое изображение, если размеры соответствуют условию
                else:
                    return None # Возвращаем None, если размеры не соответствуют условию
                
            with ThreadPoolExecutor() as executor:
                futures = []
                for image in images[:10]: # Обрабатываем только первые 10 изображений
                    future = executor.submit(process_image, image) # Отправляем изображение на обработку в отдельный поток
                    futures.append(future)

                for future in futures:
                    result = future.result() # Ожидаем завершения обработки изображения
                    if result:
                        media_group.attach_photo(result) # Прикрепляем изображение к media_group, если результат не равен None
                        
            try:
                mid = await c.message.answer_media_group(media_group)
            except Exception as e:
                loguru.logger.error(f"Cant send media group: {media_group}; e: {e}; traceback: {traceback.format_exc()}")
                mid = []
            
            s = str(random.randint(0, 99999999999))
            good_pictures_msgs = (await state.get_data()).get('good_pictures_msgs', {})
            good_pictures_msgs[s] = mid
            await state.update_data(good_pictures_msgs=good_pictures_msgs)
            
            keyboard = Keyboards.goodOptions(good, s)
            await c.message.answer(messageText, reply_markup=keyboard)
        else:
            keyboard = Keyboards.goodOptions(good)
            await c.message.answer(messageText, reply_markup=keyboard)
    elif action == "cancel_search":
        if state:
            await state.finish()
        await c.message.delete()
    elif action == "search":
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
                req = MDB.GoodsRequests.find_one(dict(ID=req_id))
                goods = list(MDB.Goods.find(dict(ProductID={"$in":req['GoodsIDs']})))
            else:
                goods = list(MDB.Goods.find(dict(GroupID=category_group_id)))
                goods = [x for x in goods if x['QtyInStore'] > 0]
            selected_brands = stateData.get("selected_brands", [])
            all_brands = set(x['Manufacturer'] for x in goods)

            await c.message.answer(Texts.BrandFilterMessage, reply_markup=Keyboards.BrandFilter(all_brands, selected_brands))  
            await state.set_state("BrandFilterState")
            await state.update_data(selected_brands=selected_brands, all_brands=all_brands, category_group_id=category_group_id)

        await c.answer()

    elif action == "brand_filter_choose":
        choosen_brand = action_params[0]
        selected_brands = stateData.get("selected_brands", [])
        all_brands = stateData.get("all_brands", [])

        if choosen_brand in selected_brands:
            selected_brands.remove(choosen_brand)
        else:
            selected_brands.append(choosen_brand)

        await c.message.edit_text(Texts.BrandFilterMessage, reply_markup=Keyboards.BrandFilter(all_brands, selected_brands))  
        await state.update_data(selected_brands=selected_brands)
        await c.answer()

    elif action == "brand_filter_show":
        selected_brands = stateData.get("selected_brands", [])
        catID = stateData['category_group_id']

        loguru.logger.info(f"See catalog goods for category {catID}")

        cat = GoodsService.GetCategoryByID(catID)
        req_id = stateData.get('req_id', None)
        if req_id is None:
            goods = list(MDB.Goods.find(dict(GroupID=cat['GroupID'])))
            if selected_brands:
                goods = [x for x in goods if x['Manufacturer'] in selected_brands]
            req_id = str(uuid4())[:9]
            MDB.GoodsRequests.insert_one(dict(
                ID=req_id,
                GoodsIDs=[x['ProductID'] for x in goods],
                CategoryID=catID,
                AppliedFilters={'BrandFilter': {"Brands": selected_brands}},
                CreatedAt=datetime.datetime.now()
            ))
        else:
            req = MDB.GoodsRequests.find_one(dict(ID=stateData['req_id']))
            goods = list(MDB.Goods.find(dict(ProductID={"$in": req['GoodsIDs']})))
            if selected_brands:
                goods = [x for x in goods if x['Manufacturer'] in selected_brands]
            req['GoodsIDs'] = [x['ProductID'] for x in goods]
            req['AppliedFilters']['BrandFilter'] = {"Brands": selected_brands}
            MDB.GoodsRequests.update_one(dict(ID=stateData['req_id']), {"$set": req})

        if not goods:
            await c.message.answer(Texts.NoGoodsForFilter, reply_markup=Keyboards.backToCategory(cat))
            return
        
        try:
            await c.message.answer(Texts.BrandsGoodsMessage.format(goods_count=len(goods)),
                                    reply_markup=Keyboards.filteredGoods(cat, goods, req_id))
        except aiogram.utils.exceptions.BadRequest as e:
            loguru.logger.error(f"{e}; {traceback.format_exc()}")
            await c.message.answer(Texts.TooManyGoodsException)

    elif action == "cancel_filter":
        await state.finish()
        await c.answer()
        await c.message.delete()

    elif action == "main":
        categories = GoodsService.GetCategoriesTree()
        await c.message.edit_text(Texts.CatalogMessage, reply_markup=Keyboards.catalog(categories))


@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE), text_contains="|FilteredGoods:", state="*")
async def _(c: CallbackQuery, state: FSMContext):
    if state:
        await state.finish()
    mode, req_id, start_index = c.data.split(":")[1:4]
    start_index = int(start_index)

    user = UserService.Get(c.from_user.id)
    request = MDB.GoodsRequests.find_one(dict(ID=req_id))
    category = GoodsService.GetCategoryByID(request['CategoryID'])
    goods = list(MDB.Goods.find(dict(ProductID={"$in": request['GoodsIDs']}, QtyInStore={"$gt": 0})))

    if mode == "left":
        start_index = max(0, start_index - 20)
    if mode == "right":
        start_index = min(len(request['GoodsIDs']), start_index + 20)

    try:
        await c.message.edit_reply_markup(reply_markup=Keyboards.filteredGoods(category, goods, req_id, start_index))
    except aiogram.utils.exceptions.BadRequest as e:
        loguru.logger.error(f"{e}; {traceback.format_exc()}")
        await c.message.answer(Texts.TooManyGoodsException)
