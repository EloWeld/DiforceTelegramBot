import base64
import loguru
from etc.filters import AntiSpam
from etc.helpers import wrap_media
from etc.keyboards import Keyboards
from loader import MDB, dp, bot

from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, CommandStart
from aiogram.types import Message, ChatType, BotCommand
from services.goodsService import GoodsService
from services.textService import Texts

from aiogram.types import Message, ChatType, BotCommand, CallbackQuery, ContentType, MediaGroup, InputFile
from services.userService import UserService
from utils import prepareGoodItemToSend, prepareUserToPrint


async def parseStartMessage(m: Message):
    if 'user_info_' in m.text:
        user = UserService.Get(m.from_user.id)
        if user.is_admin or 'admin' in user.roles:
            xUser = UserService.Get(m.text.split('user_info_')[1])
            xUser = prepareUserToPrint(xUser)
            
            await m.answer(Texts.UserInfoAdminFormat.format(user=xUser), 
                           reply_markup=Keyboards.UserInfoFromAdmin(xUser))
    if 'good_' in m.text:
        user = UserService.Get(m.from_user.id)
        goodID = m.text.split('good_')[1]
        
        good, images = GoodsService.GetGoodByID(goodID, with_images=True)
        good['Price'] = GoodsService.GetTargetPrice(user, good)
        good['ColorName'] = good['ColorName'].capitalize()
        
        messageText = prepareGoodItemToSend(good, user)
        
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
            mid = await m.answer_media_group(media_group)
            from loader import message_id_links
            message_id_links[str(mid[0].message_id)] = [x.message_id for x in mid]
            keyboard = Keyboards.goodOptions(good, mid[0].message_id)
            await m.answer(messageText, reply_markup=keyboard)
        else:
            keyboard = Keyboards.goodOptions(good)
            await m.answer(messageText, reply_markup=keyboard)

@dp.message_handler(CommandStart(), AntiSpam(), state="*")
async def _(m: Message, command: Command.CommandObj, state: FSMContext):
    if state:
        await state.finish()
        
    await parseStartMessage(m)

    # Create or UpdateUser
    user = UserService.Get(m.from_user.id)
    if not user:
        user = UserService.Create(m.from_user)
    else:
        UserService.UpdateFromTgUser(m.from_user)

    await m.answer(Texts.StartMessage, reply_markup=Keyboards.startMenu(user))
    await m.delete()

    await bot.set_my_commands([
        BotCommand("start", "Перезагрузить бота"),
        BotCommand("help", "Помощь")
    ])


@dp.callback_query_handler(lambda call: call.data.startswith('|just_hide|'))
async def _(c: CallbackQuery):
    await c.message.delete()