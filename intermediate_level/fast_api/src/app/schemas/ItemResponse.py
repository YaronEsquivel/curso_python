from pydantic import BaseModel


class ItemCreate(BaseModel):
    nombre: str
    precio: float


class ItemResponse(ItemCreate):
    id: int

    class Config:
        from_attributes = True
