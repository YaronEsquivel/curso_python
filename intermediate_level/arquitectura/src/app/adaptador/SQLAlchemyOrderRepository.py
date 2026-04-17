from app.domain import Order


class SqlAlchemyOrderRepository:
    def __init__(self, session):
        self.session = session

    def save(self, order: Order):
        self.session.add(order)
        self.session.commit()
