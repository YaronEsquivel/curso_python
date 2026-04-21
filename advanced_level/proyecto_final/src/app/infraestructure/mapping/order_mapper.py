from app.domain.entities.order import Order
from app.domain.value_objects import Money
from app.domain.value_objects.product_name import ProductName
from app.domain.value_objects.quantity import Quantity
from app.infraestructure.request.order_request import OrderRequest
from app.infraestructure.response.order_response import OrderResponse


def to_response(order: Order) -> OrderResponse:
    return OrderResponse(
        id=order.id,
        nombre=order.nombre.name,
        precio=order.precio.cantidad,
        cantidad=order.cantidad.value,
        divisa=order.precio.divisa,
        total=order.total,
    )


def from_request(order_req: OrderRequest) -> Order:
    money = Money(cantidad=order_req.precio, divisa=order_req.divisa)
    name = ProductName(name=order_req.nombre)
    quantity = Quantity(value=order_req.cantidad)
    return Order(
        precio=money,
        nombre=name,
        cantidad=quantity,
        total=money.cantidad * quantity.value,
    )
