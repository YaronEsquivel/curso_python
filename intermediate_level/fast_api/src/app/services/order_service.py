from app.models import Item, Order, OrderItem, User
from app.schemas import OrderItemResponse, OrderRequest, OrderResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_orders(db: Session):
    orders = db.query(Order).all()
    res = []
    for order in orders:
        res.append(map_to_schema(order))
    return res


def create_order(order: OrderRequest, db: Session):
    order_model = map_to_model(order)
    validate_info(order, db)
    db.add(order_model)
    db.commit()
    db.refresh(order_model)
    return map_to_schema(order_model)


def delete_order(id_order: int, db: Session):
    order = db.query(Order).filter_by(id=id_order).first()
    if not order:
        raise HTTPException(status_code=404, detail="No se encontro la orden")
    db.delete(order)
    db.commit()
    return {"message": "Se elimino la orden de forma exitosa"}


def update_order(id_order: int, order: OrderRequest, db: Session):
    old_order = db.query(Order).filter_by(id=id_order).first()
    if not old_order:
        raise HTTPException(status_code=404, detail="No se encontro la orden")
    existing_items = {item.item_id: item for item in old_order.items}
    incoming_items = {item.id_articulo: item for item in order.pedidos}

    for item_id, item_data in incoming_items.items():
        if item_id in existing_items:
            existing_items[item_id].quantity = item_data.cantidad
        else:
            new_item = OrderItem(item_id=item_id, quantity=item_data.cantidad)
            old_order.items.append(new_item)

    for item_id, db_item in existing_items.items():
        if item_id not in incoming_items:
            order.items.remove(db_item)

    db.commit()
    db.refresh(old_order)

    return map_to_schema(old_order)


def map_to_model(order: OrderRequest) -> Order:
    new_order = Order()
    items = []
    for pedido in order.pedidos:
        item = OrderItem(item_id=pedido.id_articulo, quantity=pedido.cantidad)
        items.append(item)
    new_order.items = items
    new_order.user_id = order.id_usuario
    return new_order


def map_to_schema(order: Order) -> OrderResponse:
    items = []
    for item in order.items:
        item_res = OrderItemResponse(id_articulo=item.item_id, cantidad=item.quantity)
        items.append(item_res)

    return OrderResponse(id=order.id, id_usuario=order.user_id, pedidos=items)


def validate_info(order: OrderRequest, db: Session):
    user = db.query(User).filter_by(id=order.id_usuario).first()
    if not user:
        raise HTTPException(status_code=500, detail="No se encontro el usuario")
    for pedido in order.pedidos:
        filter_item = db.query(Item).filter_by(id=pedido.id_articulo).first()
        if not filter_item:
            raise HTTPException(
                status_code=500,
                detail=f"No se encontro el articulo: {pedido.id_articulo}",
            )
