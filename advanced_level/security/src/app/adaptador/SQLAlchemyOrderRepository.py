from app.domain import Order
from app.models import OrderModel


class SqlAlchemyOrderRepository:
    def __init__(self, session):
        self.session = session

    def save(self, order: Order):
        db_order = OrderModel(user_id=order.user_id, total=order.total)

        self.session.add(db_order)
