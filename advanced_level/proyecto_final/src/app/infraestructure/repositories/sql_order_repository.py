from typing import List

from app.domain.entities.order import Order
from app.domain.repository.order_repository import OrderRepository
from app.domain.value_objects import Money
from app.domain.value_objects.product_name import ProductName
from app.domain.value_objects.quantity import Quantity
from app.infraestructure.models.order_model import OrderModel
from sqlalchemy.orm import Session


class SQLOrderRepository(OrderRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Order]:
        orders = []
        orders_model = self.db.query(OrderModel).all()
        for order_model in orders_model:
            orders.append(self.map_to_domain(order_model))
        return orders

    def save(self, new_order: Order):
        order = self.map_to_model(new_order)
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return self.map_to_domain(order)

    def delete(self, id: int):
        order = self.db.query(OrderModel).filter_by(id=id).first()
        self.db.delete(order)
        self.db.commit()

    def update(self, id: int, new_order: Order):
        order = self.map_to_model(new_order)
        output_order = self.db.query(OrderModel).filter_by(id=id).first()
        output_order.badge = order.badge
        output_order.item_name = order.item_name
        output_order.quantity = order.quantity
        output_order.unit_price = order.unit_price
        output_order.total = order.total
        self.db.add(output_order)
        self.db.commit()
        self.db.refresh(output_order)
        return self.map_to_domain(output_order)

    def map_to_domain(self, order_model: OrderModel) -> Order:
        money = Money(cantidad=order_model.unit_price, divisa=order_model.badge)
        name = ProductName(name=order_model.item_name)
        quantity = Quantity(value=order_model.quantity)
        return Order(
            precio=money,
            nombre=name,
            cantidad=quantity,
            total=money.cantidad * quantity.value,
            id=order_model.id,
        )

    def map_to_model(self, order: Order) -> OrderModel:
        return OrderModel(
            id=order.id,
            badge=order.precio.divisa,
            unit_price=order.precio.cantidad,
            total=order.total,
            quantity=order.cantidad.value,
            item_name=order.nombre.name,
        )
