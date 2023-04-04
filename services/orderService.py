import loguru
from loader import MDB
from dotdict import dotdict
from etc.helpers import rdotdict

class OrderService:
    @classmethod
    def Create(cls, order_data):
        # Создайте новый заказ на основе переданных данных
        order = dotdict(
            id=order_data['id'],
            user_id=order_data['user_id'],
            items=order_data['items'],
            created_at=order_data['created_at']
        )
        MDB.Orders.insert_one(order)
        loguru.logger.success(
            f"[ ORDER ]: Added new order, ID: {order.id}; User ID: {order.user_id}")

        return rdotdict(order)

    @classmethod
    def Get(cls, order_id):
        order = MDB.Orders.find_one(dict(id=order_id))
        return rdotdict(order) if order else None

    @classmethod
    def Update(cls, order):
        MDB.Orders.update_one(dict(id=order['id']), {"$set": dict(order)})
        loguru.logger.success(f"[ ORDER ]: Order #{order['id']} is updated")

    @classmethod
    def GetOrdersByUserId(cls, user_id):
        orders = [rdotdict(x) for x in MDB.Orders.find(dict(user_id=user_id))]
        return orders