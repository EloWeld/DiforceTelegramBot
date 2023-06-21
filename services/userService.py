import datetime
from typing import Optional, Union
import loguru
from loader import MDB
from loggerConf import logger
from dotdict import dotdict
from aiogram import types
from etc.helpers import rdotdict


SMC = Union[dict, int, str, types.Message, types.CallbackQuery]


class UserService:
    @classmethod
    def Create(cls, user: types.User):
        u = dotdict(
            id=user.id,
            username=user.username,
            fullname=user.full_name,
            is_admin=False,
            is_authenticated=False,
            opt="Retail",
            optText=None,
            roles=["user"],
            addresses=[],
            balance=0.0,
            cart={},
            last_action=datetime.datetime.now(),
            created_at=datetime.datetime.now()
        )
        MDB.Users.insert_one(u)
        logger.debug(
            f"[ USER ]: Added new user, ID: {u.id}; Username: @{u.username}")

        return rdotdict(u)

    @classmethod
    def Get(cls, user: SMC, condition: dict = None):
        from etc.helpers import rdotdict
        condition = condition if condition else dict(id=cls.GoodUser(user))
        user = MDB.Users.find_one(condition)
        return rdotdict(user) if user else None

    @classmethod
    def Update(cls, user: dict):
        MDB.Users.update_one(dict(id=user['id']), {"$set": dict(user)})
        logger.debug(f"[ USER ]: User #{user['id']} is updated")

    @classmethod
    def UpdateFromTgUser(cls, user: types.User):
        cls.Update(dict(
            id=user.id,
            fullname=user.full_name,
            username=user.username
        ))

    @classmethod
    def All(cls):
        return [rdotdict(x) for x in MDB.Users.find()]

    @classmethod
    def Admins(cls):
        admins = [rdotdict(x) for x in MDB.Users.find(dict(is_admin=True))]
        return admins

    @classmethod
    def GoodUser(cls, user: SMC):
        u_id = -1
        if isinstance(user, types.Message) or isinstance(user, types.CallbackQuery):
            u_id = user.from_user.id
        elif isinstance(user, dict) and '_id' in user:
            u_id = user['id']
        elif isinstance(user, dict) and 'id' in user:
            u_id = user['id']
        elif isinstance(user, str):
            u_id = int(user)
        elif isinstance(user, int):
            u_id = user
        return u_id

    @classmethod
    def Delete(cls, user: Union[dict, int]):
        if isinstance(user, dict):
            MDB.Users.delete_one(dict(id=user['id']))
        if isinstance(user, int):
            MDB.Users.delete_one(dict(id=user))
        logger.warning(
            f"[ USER ]: User #{user} deleted from database")

    @classmethod
    def AddToCart(cls, user_id, good):
        user = cls.Get(user_id)

        if good['ProductID'] not in user.cart:
            user.cart[good['ProductID']] = dict(
                ProductID=good['ProductID'], 
                ProductName=good['ProductName'], 
                Quantity=0)

        # Add one quantity to the cart
        user.cart[good['ProductID']]['Quantity'] += 1

        cls.Update(user)
