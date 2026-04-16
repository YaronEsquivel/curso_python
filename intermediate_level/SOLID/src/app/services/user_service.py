from app.models import User
from app.repository.SQL_user_repository import SQLUserRepository
from app.schemas.UserRequest import UserRequest
from app.schemas.UserResponse import UserResponse
from fastapi import HTTPException


class UserService:
    def __init__(self, repo: SQLUserRepository):
        self.repo = repo

    def get_users(self):
        users = self.repo.get_all()
        response = []
        for user in users:
            response.append(self.map_to_schema(user))
        return response

    def create_user(self, user: UserRequest):
        new_user = self.repo.save(self.map_to_model(user))
        return self.map_to_schema(new_user)

    def delete_user(self, id: int):
        user = self.repo.get_by_id(id)
        if not user:
            raise HTTPException(status_code=404, detail="usuario no encontrado")
        self.repo.delete(user)
        return {"message": "usuario eliminado"}

    def update_user(self, id: int, user: UserRequest):
        old_user = self.repo.get_by_id(id)
        if not old_user:
            raise HTTPException(status_code=404, detail="usuario no encontrado")
        old_user.name = user.nombre
        old_user.email = user.correo
        new_user = self.repo.save(old_user)

        return self.map_to_schema(new_user)

    def map_to_schema(self, user: User) -> UserResponse:
        res: UserResponse = UserResponse(
            nombre=user.name, correo=user.email, id=user.id
        )
        return res

    def map_to_model(self, user: UserRequest) -> User:
        res: User = User(name=user.nombre, email=user.correo)
        return res
