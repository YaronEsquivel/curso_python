from pydantic import BaseModel


class OrderDTO(BaseModel):
    user_id: int
    total: float
