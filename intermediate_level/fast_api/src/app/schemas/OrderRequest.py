from pydantic import BaseModel

from .OrderItemRequest import OrderItemRequest


class OrderRequest(BaseModel):
    id_usuario: int
    pedidos: list[OrderItemRequest]
