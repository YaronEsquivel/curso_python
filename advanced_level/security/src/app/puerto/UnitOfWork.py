from typing import Protocol

from app.puerto import OrderRepository


class UnitOfWork(Protocol):
    orders: OrderRepository

    def __enter__(self): ...

    def __exit__(self, exc_type, exc, tb): ...
