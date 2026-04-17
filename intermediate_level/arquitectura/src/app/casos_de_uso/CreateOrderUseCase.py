from app.domain import Order
from app.puerto import NotificationService, OrderRepository


class CreateOrderUseCase:
    def __init__(
        self,
        repo: OrderRepository,
        notifier: NotificationService,
    ):
        self.repo = repo
        self.notifier = notifier

    def execute(self, user_id: int, total: float):
        order = Order(user_id=user_id, total=total)

        self.repo.save(order)
        self.notifier.send_order_created(order)

        return order
