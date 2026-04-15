from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .Base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    orders = relationship("Order", back_populates="user")

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, email: {self.email}"
