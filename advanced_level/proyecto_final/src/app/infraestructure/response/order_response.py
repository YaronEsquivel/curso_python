from pydantic import BaseModel


class OrderResponse(BaseModel):
    id: int
    nombre: str
    precio: float
    cantidad: int
    total: float
    divisa: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Laptop",
                "precio": 1500.0,
                "cantidad": 2,
                "total": 3000.0,
                "divisa": "USD",
            }
        }
