from app.models import User
from sqlalchemy.orm import Session


class SQLUserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(User).all()

    def get_by_id(self, id: int):
        return self.db.query(User).filter_by(id=id).first()

    def save(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: User):
        self.db.delete(user)
        self.db.commit()
