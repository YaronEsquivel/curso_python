from typing import Protocol

from app.domain import Order


class NotificationService(Protocol):
    def send_order_created(self, order: Order) -> None: ...
