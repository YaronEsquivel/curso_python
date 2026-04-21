from app.infraestructure.models.order_model import OrderModel


class InMemoryOrderRepository:
    def __init__(self):
        self.orders = []
        self.counter = 1

    def get_all(self):
        return self.orders

    def get_by_id(self, id: int):
        return next((o for o in self.orders if o.id == id), None)

    def save(self, order: OrderModel):
        order.id = self.counter
        self.counter += 1
        self.orders.append(order)
        return order

    def delete(self, id: int):
        order = self.get_by_id(id)
        if order is None:
            return None
        self.orders.remove(order)

    def update(self, id: int, order: OrderModel):
        old_order = self.get_by_id(id)

        if old_order is None:
            return None

        old_order.item_name = order.item_name
        old_order.unit_price = order.unit_price
        old_order.quantity = order.quantity
        old_order.total = order.unit_price * order.quantity

        return old_order
