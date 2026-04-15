from pydantic import BaseModel, Field


class ItemRequest(BaseModel):
    nombre: str = Field(min_length=3, max_length=50)
    precio: float

    class Config:
        from_attributes = True
