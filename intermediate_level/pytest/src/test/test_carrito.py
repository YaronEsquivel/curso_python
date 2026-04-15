from app.carrito import calcular_total
from hypothesis import given
from hypothesis.strategies import fixed_dictionaries, integers, lists


def test_total():
    items = [{"precio": 10, "cantidad": 5}, {"precio": 20, "cantidad": 2}]
    assert calcular_total(items) == 90


@given(
    lists(
        fixed_dictionaries(
            {
                "precio": integers(min_value=0, max_value=100),
                "cantidad": integers(min_value=0, max_value=100),
            }
        )
    )
)
def test_total_no_negativo(items):
    assert calcular_total(items) >= 0
