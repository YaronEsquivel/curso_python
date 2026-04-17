from typing import Protocol

from app.domain import Order


class OrderRepository(Protocol):
    def save(self, order: Order) -> None: ...
