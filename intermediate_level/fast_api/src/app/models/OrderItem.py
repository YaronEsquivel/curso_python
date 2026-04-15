from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .Base import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    quantity = Column(Integer)

    order = relationship("Order", back_populates="items")
    item = relationship("Item", back_populates="order_items")

    def __str__(self):
        return f"id: {self.id}, order_id: {self.order_id}, item_id: {self.item_id}, quantity: {self.quantity}"
