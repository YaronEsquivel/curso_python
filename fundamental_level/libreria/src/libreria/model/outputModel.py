from typing import Optional

from pydantic import BaseModel


class OutputModel(BaseModel):
    metrics: Optional[dict[str, float]] = None
    by_status: Optional[dict[str, int]] = None
    top_users: Optional[list[dict[str, int | float]]] = None
