from sqlalchemy import Column, Float, Integer

from .Base import Base


class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    total = Column(Float)
