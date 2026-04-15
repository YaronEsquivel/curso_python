from pydantic import BaseModel


class OrderItemResponse(BaseModel):
    id_articulo: int
    cantidad: int

    class Config:
        from_attributes = True
