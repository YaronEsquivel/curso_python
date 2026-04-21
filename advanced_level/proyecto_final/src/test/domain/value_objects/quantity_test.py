import pytest
from app.domain.value_objects.quantity import Quantity


def test_quantity_valid():
    quantity = Quantity(value=5)
    assert quantity.value == 5


def test_quantity_empty():
    with pytest.raises(ValueError):
        Quantity(-1)
