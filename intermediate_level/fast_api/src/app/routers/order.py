from app import facade, schemas
from app.core.security import decode_token
from app.dependencies.db import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

router = APIRouter(prefix="/orders", tags=["Orders"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


@router.get("/", response_model=list[schemas.OrderResponse])
def get_orders(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return facade.order_facade.get_orders(db)


@router.post(
    "/", response_model=schemas.OrderResponse, status_code=status.HTTP_201_CREATED
)
def create_order(
    order: schemas.OrderRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return facade.order_facade.create_order(order, db)


@router.delete("/{id_order}", response_model=dict, status_code=status.HTTP_200_OK)
def delete_order(
    id_order: int, db: Session = Depends(get_db), user=Depends(get_current_user)
):
    return facade.order_facade.delete_order(id_order, db)


@router.put(
    "/{id_order}",
    response_model=schemas.OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
def update_order(
    id_order: int,
    order: schemas.OrderRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return facade.order_facade.update_order(id_order, order, db)
