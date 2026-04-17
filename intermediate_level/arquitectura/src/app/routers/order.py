from app import DTO
from app.adaptador import FakeNotificationService, SqlAlchemyOrderRepository
from app.casos_de_uso import CreateOrderUseCase
from app.core.security import decode_token
from app.dependencies.db import get_db
from app.DTO import OrderDTO
from app.puerto import NotificationService, OrderRepository
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

router = APIRouter(prefix="/orders", tags=["Orders"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_order_repo(db: Session = Depends(get_db)):
    return SqlAlchemyOrderRepository(db)


def get_notify_service():
    return FakeNotificationService()


def get_save_use_case(
    repository: OrderRepository = Depends(get_order_repo),
    notifySvc: NotificationService = Depends(get_notify_service),
):
    return CreateOrderUseCase(repository, notifySvc)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


@router.post("/", response_model=DTO.OrderDTO, status_code=status.HTTP_201_CREATED)
def create_user(
    response: Response,
    order: OrderDTO,
    user=Depends(get_current_user),
    use_case=Depends(get_save_use_case),
):
    created_order = use_case.execute(order)
    return created_order
