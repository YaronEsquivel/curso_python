from pydantic import BaseModel


class OrderItemRequest(BaseModel):
    id_articulo: int
    cantidad: int
