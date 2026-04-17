from app.domain import Order


class InMemoryOrderRepository:
    def __init__(self):
        self.orders = []

    def save(self, order: Order):
        self.orders.append(order)
