import pytest
from app.domain.value_objects.product_name import ProductName


def test_product_name_valid():
    name = ProductName(name="Laptop")
    assert str(name) == "Laptop"


def test_product_name_empty():
    with pytest.raises(ValueError):
        ProductName(name="")


def test_product_name_too_long():
    with pytest.raises(ValueError):
        ProductName(name="qwertyuiopasdfghjklñzxcvbnmqwertyuiopasdfghjkl")
