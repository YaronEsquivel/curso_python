from app.domain.entities.order import Order
from app.domain.repository.order_repository import OrderRepository


class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def get_all(self):
        return self.order_repository.get_all()

    def save(self, order: Order):
        return self.order_repository.save(order)

    def delete(self, id: int):
        return self.order_repository.delete(id)

    def update(self, id: int, order: Order):
        return self.order_repository.update(id, order)
