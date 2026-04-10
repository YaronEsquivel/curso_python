from pydantic import BaseModel


class OrderIn(BaseModel):
    product: str
    quantity: int
    unit_price: float
