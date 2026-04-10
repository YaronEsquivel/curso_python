from dataclasses import dataclass


@dataclass
class Order:
    id: int
    product_name: str
    quantity: int
    price: float
    iva: int = 16

    @property
    def total(self):
        return (self.price * self.quantity) * (1 + self.iva / 100)

    def __str__(self):
        return f"El {self.product_name} cuesta {self.price}, se compraron {self.quantity}, con un iva de {self.iva}%, el total gastado es {self.total}"

    def __eq__(self, other):
        if not isinstance(other, Order):
            return NotImplemented
        return self.total == other.total

    def __lt__(self, other):
        if not isinstance(other, Order):
            return NotImplemented
        return self.total < other.total

    def __gt__(self, other):
        if not isinstance(other, Order):
            return NotImplemented
        return self.total > other.total
