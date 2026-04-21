from dataclasses import dataclass

from app.domain.value_objects import Money, ProductName, Quantity


@dataclass
class Order:
    precio: Money
    nombre: ProductName
    cantidad: Quantity
    total: float
    id: int | None = None
