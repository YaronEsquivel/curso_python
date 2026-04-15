from app.models import User
from app.schemas.UserRequest import UserRequest
from app.schemas.UserResponse import UserResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_users(db: Session):
    users = db.query(User).all()
    response = []
    for user in users:
        response.append(map_to_schema(user))
    return response


def create_user(user: UserRequest, db: Session):
    new_user = map_to_model(user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return map_to_schema(new_user)


def delete_user(id: int, db: Session):
    user = db.query(User).filter_by(id=id).first()
    if not user:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"message": "usuario eliminado"}


def update_user(id: int, user: UserRequest, db: Session):
    old_user = db.query(User).filter_by(id=id).first()
    if not old_user:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    old_user.name = user.nombre
    old_user.email = user.correo

    db.commit()
    db.refresh(old_user)

    return map_to_schema(old_user)


def map_to_schema(user: User) -> UserResponse:
    res: UserResponse = UserResponse(nombre=user.name, correo=user.email, id=user.id)
    return res


def map_to_model(user: UserRequest) -> User:
    res: User = User(name=user.nombre, email=user.correo)
    return res
