from pydantic import BaseModel


class OrderOut(BaseModel):
    id: int
    producto: str
    cantidad: int
    precio_unitario: float
    total: float
