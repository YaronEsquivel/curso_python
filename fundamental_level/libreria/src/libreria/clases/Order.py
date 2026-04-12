from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    order_id: int
    user_id: int
    amount: float
    status: str
    created_at: datetime
