from app import facade, schemas
from app.core.security import decode_token
from app.dependencies.db import get_db
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


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
def get_users(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return facade.user_facade.get_users(db)


@router.post(
    "/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED
)
def create_user(
    new_user: schemas.UserRequest,
    response: Response,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    created_user = facade.user_facade.create_user(new_user, db)
    response.headers["Location"] = f"/users/{created_user.id}"
    return created_user


@router.delete("/{id_user}", response_model=dict, status_code=status.HTTP_200_OK)
def delete_user(
    id_user: int, db: Session = Depends(get_db), user=Depends(get_current_user)
):
    return facade.user_facade.delete_user(id_user, db)


@router.put(
    "/{id_user}", response_model=schemas.UserResponse, status_code=status.HTTP_200_OK
)
def update_user(
    id_user: int,
    update_user: schemas.UserRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    new_user = facade.user_facade.update_user(id_user, update_user, db)
    return new_user
