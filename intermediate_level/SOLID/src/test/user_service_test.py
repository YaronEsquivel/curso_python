from app.repository import MemoryUserRepository
from app.schemas.UserRequest import UserRequest
from app.services import UserService


def test_get_user():
    repo = MemoryUserRepository()
    service = UserService(repo)

    service.create_user(UserRequest(nombre="nombre", correo="correo@correo.com"))

    assert len(service.get_users()) == 1
