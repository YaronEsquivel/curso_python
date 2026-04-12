from pydantic import BaseModel


class OrderIn(BaseModel):
    order_id: str
    user_id: str
    amount: str
    status: str
    created_at: str
