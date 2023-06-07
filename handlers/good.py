from concurrent.futures import ThreadPoolExecutor
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
from PIL import Image, UnidentifiedImageError
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
from utils import cutText, prepareCartItemToSend, prepareGoodItemToSend, tryDelete

@dp.callback_query_handler(ChatTypeFilter(ChatType.PRIVATE), text_contains="|Good:", state="*")
async def _(c: CallbackQuery, state: FSMContext):
    global message_id_links
    action = c.data.split(":")[1]
    user = UserService.Get(c)

    if action == "add_to_cart":
        goodID = c.data.split(":")[2]
        good = GoodsService.GetGoodByID(goodID)
        if good['QtyInStore'] == 0:
            await c.answer()
            await c.message.answer("❌ Товара нет на складе, добавить в корзину невозможно")
            return
        await c.answer(Texts.AddedToCart)
        UserService.AddToCart(user.id, good)
        user = UserService.Get(user.id)
        text = prepareCartItemToSend(good, [user['cart'][x] for x in user['cart'] if x == goodID][0], user)
        await c.message.edit_text(text, reply_markup = Keyboards.goodOptions(user, good, media_group_message_id=c.data.split(":")[3]))
        

    if action == "found_cheaper":
        await c.answer()
        goodID = c.data.split(":")[2]
        await state.set_state("FoundItCheaper")
        ans_msg = await c.message.answer(Texts.FoundCheaperMessage, reply_markup=Keyboards.foundCheaperMenu())
        await state.update_data(goodID=goodID, msgID=ans_msg.message_id)
    
    if action == "see_other_photos":
        await c.answer("📷 Фотографии загружаются...")
        goodID = c.data.split(":")[2]
        mg = MediaGroup()
        good, images = GoodsService.GetGoodByID(goodID, True)
        if images:
            media_group = MediaGroup()
            
            def process_image(image):
                b_img = base64.b64decode(image)
                try:
                    img = Image.open(BytesIO(b_img))
                except UnidentifiedImageError:
                    loguru.logger.error('Failed to identify the image')
                    return None
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
            sessionID = c.data.split(":")[3]
            sessionID2 = str(uuid4())[:10]
            txtMsg = await c.message.answer(f"📷⤴️ Дополнительные фотографии к товару <b>{cutText(good['ProductName'], 50)}</b> <i>({good['ProductArt']})</i>", reply_markup=Keyboards.hideAdditionalPhotos(sessionID2))
            
            additionalInfoMessages = mid + [txtMsg]
            
            good_pictures_msgs = (await state.get_data()).get('good_pictures_msgs', {})
            good_pictures_msgs[sessionID2] = additionalInfoMessages
            if sessionID in good_pictures_msgs:
                good_pictures_msgs[sessionID].extend(additionalInfoMessages)
            await state.update_data(good_pictures_msgs=good_pictures_msgs)

    if action == "hide":
        await c.answer()
        mid = c.data.split(":")[2]
        stateData = await state.get_data()
        good_pictures_msgs = stateData.get('good_pictures_msgs', {})
        if mid in good_pictures_msgs:
            for good_msg in good_pictures_msgs[mid][::-1]:
                await tryDelete(good_msg)
        await tryDelete(c.message)
    

# =============== FOUND CHEAPER ===============

@dp.message_handler(ChatTypeFilter(ChatType.PRIVATE), content_types=[ContentType.TEXT, ContentType.PHOTO], state="FoundItCheaper")
async def _(m: Message, state: FSMContext):
    stateData = dotdict(await state.get_data())
    user = UserService.Get(m.from_user.id)
    if m.text == Texts.QuitButton:
        await m.answer('👌🏻', reply_markup=Keyboards.startMenu(user))
        await m.delete()
        await bot.delete_message(m.chat.id, stateData.msgID)
        return
    good = GoodsService.GetGoodByID(stateData.goodID)
    comment = m.text if m.text else m.caption if m.caption else '➖'
    # Define admin type for send message

    # Build text
    messageText = Texts.FoundCheaperAdminMessage.format(
        good=good, user=user, comment=comment, BotUsername=Consts.BotUsername)

    # If has attached photo - send photo
    if len(m.photo) > 0:
        await bot.send_photo(Consts.OrderManagerID, caption=messageText, photo=m.photo[0].file_id)
    else:
        await bot.send_message(Consts.OrderManagerID, text=messageText)
    await m.answer(Texts.YourRequestWasSentMessage, reply_markup=Keyboards.startMenu(user))
