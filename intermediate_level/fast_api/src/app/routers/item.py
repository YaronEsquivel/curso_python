from app import facade, schemas
from app.core.security import decode_token
from app.dependencies.db import get_db
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

router = APIRouter(prefix="/items", tags=["Items"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


@router.get("/", response_model=list[schemas.ItemResponse])
def get_users(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return facade.item_facade.get_items(db)


@router.post(
    "/", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED
)
def create_item(
    item: schemas.ItemRequest,
    response: Response,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    new_item = facade.item_facade.create_item(item, db)
    response.headers["Location"] = f"/users/{new_item.id}"
    return new_item


@router.delete("/{id_item}", response_model=dict, status_code=status.HTTP_200_OK)
def delete_item(
    id_item: int, db: Session = Depends(get_db), user=Depends(get_current_user)
):
    return facade.item_facade.delete_item(id_item, db)


@router.put(
    "/{id_item}", response_model=schemas.ItemResponse, status_code=status.HTTP_200_OK
)
def update_user(
    id_item: int,
    item: schemas.ItemRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    new_item = facade.item_facade.update_item(id_item, item, db)
    return new_item
