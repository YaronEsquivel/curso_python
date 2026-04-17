from app.models import User


class MemoryUserRepository:
    def __init__(self):
        self.users = []
        self.counter = 1

    def get_all(self):
        return self.users

    def get_by_id(self, id: int):
        return next((u for u in self.users if u.id == id), None)

    def save(self, user: User):
        user.id = self.counter
        self.counter += 1
        self.users.append(user)
        return user

    def delete(self, user: User):
        self.users.remove(user)
