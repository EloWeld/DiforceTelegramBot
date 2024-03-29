from typing import Union
from dotdict import dotdict
from datetime import datetime, timedelta

import loguru
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery
from loggerConf import logger

usersMsgData = dotdict()
banTime = 5
allowedTime = 1
spamBufferSize = 3


class Admin(BoundFilter):
    async def check(self, m: Union[Message, CallbackQuery]) -> bool:
        user_id = m.from_user.id
        from services.userService import UserService
        user = UserService.Get(user_id)
        return user and (user.is_admin or 'admin' in user.roles)
    
class AntiSpam(BoundFilter):
    async def check(self, m: Message) -> bool:
        user = m.from_user.id
        allow = True
        if user in usersMsgData:
            if datetime.now() < usersMsgData[user].banExpire:
                # User in ban
                allow = False
            else:
                last = usersMsgData[user].lastMsgs
                if datetime.now().timestamp() - (sum(last) / len(last)) < allowedTime:
                    # Detected Spam
                    try:
                        await m.reply("Пожалуйста, не спамьте!")
                    except Exception as e:
                        logger.debug(f"[ ANTI-SPAM ]: Can't reply to message {m.message_id} | {e}")
                    usersMsgData[user].banExpire = datetime.now() + timedelta(seconds=banTime)
                    allow = False
        else:
            # Add to check
            usersMsgData[user] = dotdict(lastMsgs=[datetime.now().timestamp()],
                                         banExpire=datetime.now() - timedelta(seconds=10))
        usersMsgData[user].lastMsgs = usersMsgData[user].lastMsgs[-spamBufferSize:] + [datetime.now().timestamp()]
        return allow
