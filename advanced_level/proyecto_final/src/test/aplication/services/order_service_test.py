from app.aplication.services.order_service import OrderService
from app.infraestructure.models.order_model import OrderModel
from app.infraestructure.repositories.in_memory_repository import (
    InMemoryOrderRepository,
)


def test_inject_service():
    repo = InMemoryOrderRepository()
    assert OrderService(repo)


def test_get_all():
    repo = InMemoryOrderRepository()
    service = OrderService(repo)
    assert len(service.get_all()) == 0


def test_save():
    repo = InMemoryOrderRepository()
    service = OrderService(repo)
    order = OrderModel(badge="MXN", unit_price=20000, quantity=5, item_name="Laptop")
    service.save(order)
    assert len(service.get_all()) == 1


def test_delete():
    repo = InMemoryOrderRepository()
    service = OrderService(repo)
    order = OrderModel(badge="MXN", unit_price=20000, quantity=5, item_name="Laptop")
    service.save(order)
    assert service.delete(1) is None
    assert len(service.get_all()) == 0


def test_update():
    repo = InMemoryOrderRepository()
    service = OrderService(repo)
    order = OrderModel(badge="MXN", unit_price=2000, quantity=5, item_name="Laptop")
    service.save(order)
    updated_order = OrderModel(
        badge="DLS", unit_price=20000, quantity=5, item_name="Laptop"
    )
    service.update(1, updated_order)
    assert service.get_all()[0].total == 100000


def test_update_wrong_id():
    repo = InMemoryOrderRepository()
    service = OrderService(repo)
    order = OrderModel(badge="MXN", unit_price=2000, quantity=5, item_name="Laptop")
    service.save(order)
    updated_order = OrderModel(
        badge="DLS", unit_price=20000, quantity=5, item_name="Laptop"
    )
    assert service.update(10, updated_order) is None


def test_delete_wrong_id():
    repo = InMemoryOrderRepository()
    service = OrderService(repo)
    assert service.delete(10) is None
