from pydantic import BaseModel

from .OrderItemResponse import OrderItemResponse


class OrderResponse(BaseModel):
    id: int
    id_usuario: int
    pedidos: list[OrderItemResponse]

    class Config:
        from_attributes = True
