import datetime
import loguru
from loader import MDB
from dotdict import dotdict
from etc.helpers import rdotdict
from services.oneService import OneService


class OrderService:
    @classmethod
    def CreateFromDiforce(cls, order_data):
        # Создайте новый заказ на основе переданных данных
        order = dict(
            id=order_data['id'],
            user_id=None,
            created_with_bot=False,
            diforce_user_id=order_data['ContragentID'],
            amount=order_data['Amount'],
            created_at=datetime.datetime.strptime(
                order_data['PaymentDate'], "%d.%m.%Y %H:%M:%S"),
            items=[dict(
                id=x['ProductID'],
                name=x['ProductName'], summary=x['Summary'],
                qty=x['Quantity'],
                price=x['Price']) for x in order_data['Products']]
        )
        return rdotdict(order)
    
   
    @classmethod
    def CreateWithBot(cls, diforce_data, user):
        data = OneService.GetOrder(diforce_data['CreatedOrderID'], user.diforce_data.ID)
        data['id'] = diforce_data['CreatedOrderID']
        order = cls.CreateFromDiforce(data)
        if order is None:
            return None
        order['created_with_bot'] = True
        order['created_date'] = datetime.datetime.now()##datetime.datetime.strptime(diforce_data['CreatedOrderDate'], "%Y-%m-%dT%H:%M:%S")
        return rdotdict(order)

    @classmethod
    def Get(cls, order_id, diforce_user_id):
        order = MDB.Orders.find_one(dict(id=order_id))
        if order is None:
            order = OneService.GetOrder(order_id, diforce_user_id)
            order['id'] = order_id
            order = cls.CreateFromDiforce(order)
        return rdotdict(order) if order else None

    @classmethod
    def Update(cls, order):
        MDB.Orders.update_one(dict(id=order['id']), {"$set": dict(order)})
        loguru.logger.success(f"[ ORDER ]: Order #{order['id']} is updated")

    @classmethod
    def GetOrdersByUser(cls, user):
        user_id = user.id
        orders = OneService.GetOrdersByUser(user)
        orders = [rdotdict(dict(
            id=x['OrderID'].split(' ')[2],
            created_with_bot=False,
            user_id=user.id,
            items=[],
            created_at=datetime.datetime.strptime(
                x['OrderID'].split('от ')[1], '%d.%m.%Y %H:%M:%S')
        )) for x in orders]
        m_orders = [rdotdict(x)
                    for x in MDB.Orders.find(dict(user_id=user_id))]
        m_orders_ids = [x['id'] for x in m_orders]
        for x in orders:
            if x['id'] in m_orders_ids:
                x['created_with_bot'] = True
        return orders
