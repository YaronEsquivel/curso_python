from app.infraestructure.models.base import Base
from sqlalchemy import Column, Float, Integer, String


class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    badge = Column(String)
    unit_price = Column(Float)
    total = Column(Float)
    quantity = Column(Integer)
    item_name = Column(String)
