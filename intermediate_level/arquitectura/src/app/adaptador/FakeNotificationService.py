from app.domain import Order


class FakeNotificationService:
    def send_order_created(self, order: Order):
        print("Notificación enviada")
