from app.schemas.UserRequest import UserRequest
from app.services import UserService


class UserFacade:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_users(self):
        return self.user_service.get_users()

    def create_user(self, user: UserRequest):
        return self.user_service.create_user(user)

    def delete_user(self, id: int):
        return self.user_service.delete_user(id)

    def update_user(self, id: int, user: UserRequest):
        return self.user_service.update_user(id, user)
