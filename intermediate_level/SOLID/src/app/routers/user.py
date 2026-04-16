from app import schemas
from app.core.security import decode_token
from app.dependencies.db import get_db
from app.facade.user_facade import UserFacade
from app.repository import SQL_user_repository
from app.repository.user_repository import UserRepository
from app.services.user_service import UserService
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_user_repo(db: Session = Depends(get_db)):
    return SQL_user_repository(db)


def get_user_service(repository: UserRepository = Depends(get_user_repo)):
    return UserService(repository)


def get_user_facade(service: UserService = Depends(get_user_service)):
    return UserFacade(service)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return user


@router.get("/", response_model=list[schemas.UserResponse])
def get_users(
    facade: UserFacade = Depends(get_user_facade), user=Depends(get_current_user)
):
    return facade.get_users()


@router.post(
    "/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED
)
def create_user(
    new_user: schemas.UserRequest,
    response: Response,
    facade: UserFacade = Depends(get_user_facade),
    user=Depends(get_current_user),
):
    created_user = facade.create_user(new_user)
    response.headers["Location"] = f"/users/{created_user.id}"
    return created_user


@router.delete("/{id_user}", response_model=dict, status_code=status.HTTP_200_OK)
def delete_user(
    id_user: int,
    facade: UserFacade = Depends(get_user_facade),
    user=Depends(get_current_user),
):
    return facade.delete_user(id_user)


@router.put(
    "/{id_user}", response_model=schemas.UserResponse, status_code=status.HTTP_200_OK
)
def update_user(
    id_user: int,
    update_user: schemas.UserRequest,
    facade: UserFacade = Depends(get_user_facade),
    user=Depends(get_current_user),
):
    new_user = facade.update_user(id_user, update_user)
    return new_user
