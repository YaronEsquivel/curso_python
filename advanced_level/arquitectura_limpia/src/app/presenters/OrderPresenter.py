from app.domain import Order


class OrderPresenter:
    def presenter(self, order: Order):
        return {"user_id": order.user_id, "total": order.total, "status": "created"}
