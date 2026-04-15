from app.models import Item
from app.schemas import ItemRequest, ItemResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_items(db: Session):
    items = db.query(Item).all()
    response = []
    for item in items:
        response.append(map_to_schema(item))
    return response


def create_item(item: ItemRequest, db: Session):
    new_item = map_to_model(item)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return map_to_schema(new_item)


def delete_item(id: int, db: Session):
    item = db.query(Item).filter_by(id=id).first()
    if not item:
        raise HTTPException(status_code=404, detail="item no encontrado")
    db.delete(item)
    db.commit()
    return {"message": "item eliminado"}


def update_item(id: int, item: ItemRequest, db: Session):
    old_item = db.query(Item).filter_by(id=id).first()
    if not old_item:
        raise HTTPException(status_code=404, detail="item no encontrado")
    old_item.name = item.nombre
    old_item.price = item.precio

    db.commit()
    db.refresh(old_item)

    return map_to_schema(old_item)


def map_to_schema(item: Item) -> ItemResponse:
    res: ItemResponse = ItemResponse(nombre=item.name, precio=item.price, id=item.id)
    return res


def map_to_model(item: ItemRequest) -> Item:
    res: Item = Item(name=item.nombre, price=item.precio)
    return res
