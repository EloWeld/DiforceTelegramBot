import datetime
from typing import Union
import loguru
from loader import MDB
from dotdict import dotdict
from aiogram import types


SMC = Union[dict, int, str, types.Message, types.CallbackQuery]


class User:
    @classmethod
    def Create(cls, user: types.User):
        u = dotdict(
            TGID=user.id,
            Username=user.username,
            Fullname=user.full_name,
            Role="USER",
            Inviter=0,
            Invites=[],
            Balance=0.0,
            Cart={},
            Settings=dict(currency="RUB",
                            delivery="AIRPLANE",
                            insurance=True),
            CreatedAt=datetime.datetime.now()
        )
        loguru.logger.success(f"[ USER ]: Added new user, ID: {u.TGID}; Username: @{u.Username}")
        return MDB.Users.insert_one(u)

    @classmethod
    def Get(cls, user: SMC, condition: dict = None):
        from etc.helpers import RDotDict
        condition = condition if condition else dict(TGID=User.GoodUser(user))
        r = MDB.Users.find_one(condition)
        return RDotDict(r) if r else None

    @classmethod
    def Update(cls, user: SMC, changes=None):
        u_id = User.GoodUser(user)
        print(u_id, user)
        if not changes:
            MDB.Users.update_one(dict(TGID=u_id), {"$set": dict(user)})
        else:
            MDB.Users.update_one(dict(TGID=u_id), {"$set": dict(changes)})

    @classmethod
    def All(cls):
        from etc.helpers import RDotDict
        return [RDotDict(x) for x in MDB.Users.find()]

    @classmethod
    def Admins(cls):
        from etc.helpers import RDotDict
        admins = [RDotDict(x) for x in MDB.Users.find(dict(Role="ADMIN"))]
        return admins

    @classmethod
    def GoodUser(cls, user: SMC):
        u_id = -1
        if isinstance(user, types.Message) or isinstance(user, types.CallbackQuery):
            u_id = user.from_user.id
        elif isinstance(user, dict) and '_id' in user:
            u_id = user['TGID']
        elif isinstance(user, dict) and 'TGID' in user:
            u_id = user['TGID']
        elif isinstance(user, str):
            u_id = int(user)
        elif isinstance(user, int):
            u_id = user
        return u_id

    @classmethod
    def Delete(cls, conditions: dict):
        MDB.Users.delete_one(conditions)