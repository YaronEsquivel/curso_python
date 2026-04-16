from sqlalchemy import Column, Integer, String

from .Base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, email: {self.email}"
