from app.aplication.services.order_service import OrderService
from app.infraestructure.db.db import get_db
from app.infraestructure.mapping.order_mapper import from_request, to_response
from app.infraestructure.repositories.sql_order_repository import SQLOrderRepository
from app.infraestructure.request.order_request import OrderRequest
from app.infraestructure.response.order_response import OrderResponse
from app.infraestructure.security.security import decode_token
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

router = APIRouter(prefix="/orders", tags=["Orders"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


def get_repo(session=Depends(get_db)):
    return SQLOrderRepository(session)


def get_service(repo: SQLOrderRepository = Depends(get_repo)):
    return OrderService(repo)


@router.get(
    "/",
    response_model=list[OrderResponse],
    summary="Obtener ordenes",
    description="Obtiene una lista de todas las ordenes registradas",
)
def get_orders(
    service: OrderService = Depends(get_service), user=Depends(get_current_user)
):
    orders = service.get_all()
    return [to_response(order) for order in orders]


@router.post(
    "/",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear orden",
    description="Crea una nueva orden con los parametros requeridos",
)
def create_order(
    order: OrderRequest,
    service: OrderService = Depends(get_service),
    user=Depends(get_current_user),
):
    req = from_request(order)
    order_res = service.save(req)
    return to_response(order_res)


@router.delete(
    "/{id_order}",
    response_model=dict,
    status_code=status.HTTP_200_OK,
    summary="Borrar orden",
    description="Borra una orden por medio de su id",
)
def delete_order(
    id_order: int,
    service: OrderService = Depends(get_service),
    user=Depends(get_current_user),
):
    service.delete(id_order)
    return {"message": "elemento eliminado"}


@router.put(
    "/{id_order}",
    response_model=OrderResponse,
    status_code=status.HTTP_200_OK,
    summary="Actualizar orden",
    description="Se requiere una orden y el id para recuperar la orden y actualizarla con la nueva información",
)
def update_order(
    id_order: int,
    order: OrderRequest,
    service: OrderService = Depends(get_service),
    user=Depends(get_current_user),
):
    new_order = from_request(order)
    return to_response(service.update(id_order, new_order))
