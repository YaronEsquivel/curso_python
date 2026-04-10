from dataclasses import dataclass


@dataclass
class Order:
    id: int
    product: str
    quantity: int
    unit_price: float

    @property
    def total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"Id: {self.id}, producto: {self.product}, cantidad: {self.quantity}, precio unitario: {self.unit_price}, costo total: {self.total}"
