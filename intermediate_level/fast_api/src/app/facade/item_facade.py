from app import services
from app.schemas.ItemRequest import ItemRequest
from sqlalchemy.orm import Session


def get_items(db: Session):
    return services.item_service.get_items(db)


def create_item(item: ItemRequest, db: Session):
    return services.item_service.create_item(item, db)


def delete_item(id: int, db: Session):
    return services.item_service.delete_item(id, db)


def update_item(id: int, item: ItemRequest, db: Session):
    return services.item_service.update_item(id, item, db)
