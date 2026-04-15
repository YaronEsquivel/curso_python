from app import services
from app.schemas import OrderRequest
from sqlalchemy.orm import Session


def get_orders(db: Session):
    return services.order_service.get_orders(db)


def create_order(order: OrderRequest, db: Session):
    return services.order_service.create_order(order, db)


def delete_order(id_order: int, db: Session):
    return services.order_service.delete_order(id_order, db)


def update_order(id_order: int, order: OrderRequest, db: Session):
    return services.order_service.update_order(id_order, order, db)
