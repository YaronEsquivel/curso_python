from app.infraestructure.repositories.in_memory_repository import (
    InMemoryOrderRepository,
)
from app.infraestructure.routers.order_routers import get_current_user, get_repo
from app.main import app
from fastapi.testclient import TestClient

app.dependency_overrides[get_current_user] = lambda: {"sub": "test-user"}

fake_repo = InMemoryOrderRepository()


def override_get_repository():
    return fake_repo


app.dependency_overrides[get_repo] = override_get_repository

client = TestClient(app)


def test_get_orders():
    client.post(
        "/orders",
        json={"nombre": "Laptop", "precio": 1000, "cantidad": 3, "divisa": "MXN"},
    )
    response = client.get("/orders")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_create_order():
    response = client.post(
        "/orders/",
        json={"nombre": "Laptop", "precio": 1000, "cantidad": 3, "divisa": "MXN"},
    )

    assert response.status_code == 201

    data = response.json()
    assert data["nombre"] == "Laptop"
    assert data["total"] == 3000


def test_update_order():
    client.post(
        "/orders",
        json={"nombre": "Laptop", "precio": 1000, "cantidad": 1, "divisa": "MXN"},
    )
    updated_response = client.put(
        "/orders/1",
        json={"nombre": "PC", "precio": 2000, "cantidad": 10, "divisa": "USD"},
    )
    assert updated_response.status_code == 200

    data = updated_response.json()
    assert data["nombre"] == "PC"


def test_delete_order():
    client.post(
        "/orders",
        json={"nombre": "Laptop", "precio": 1000, "cantidad": 1, "divisa": "MXN"},
    )
    response = client.delete(
        "/orders/1",
    )
    assert response.status_code == 200
