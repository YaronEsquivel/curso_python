from app import services
from app.schemas.UserRequest import UserRequest
from sqlalchemy.orm import Session


def get_users(db: Session):
    return services.user_service.get_users(db)


def create_user(user: UserRequest, db: Session):
    return services.user_service.create_user(user, db)


def delete_user(id: int, db: Session):
    return services.user_service.delete_user(id, db)


def update_user(id: int, user: UserRequest, db: Session):
    return services.user_service.update_user(id, user, db)
