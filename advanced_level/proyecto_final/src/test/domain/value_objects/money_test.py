import pytest
from app.domain.value_objects.money import Money


def test_money_valid():
    precio = Money(cantidad=10, divisa="MXN")
    assert str(precio.divisa) == "MXN"
    assert precio.cantidad == 10


def test_money_quantity_empty():
    with pytest.raises(ValueError):
        Money(-1, "MXN")


def test_money_badge_empty():
    with pytest.raises(ValueError):
        Money(10, "")
