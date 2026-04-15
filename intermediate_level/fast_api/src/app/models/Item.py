from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship

from .Base import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    order_items = relationship(
        "OrderItem", back_populates="item", cascade="all, delete"
    )

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name} price: {self.price}"
