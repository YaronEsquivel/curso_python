from pydantic import BaseModel


class OrderRequest(BaseModel):
    nombre: str
    precio: float
    cantidad: int
    divisa: str

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Laptop",
                "precio": 1500,
                "cantidad": 2,
                "divisa": "MXN",
            }
        }
