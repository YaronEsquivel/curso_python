from ..clases.Order import Order


def main():
    velas = Order(1, "Candelaria", 2, 9.10)
    lechuga = Order(2, "Lechuga", 5, 20, 0)
    huevo = Order(3, "Huevo", 2, 50, 0)

    print(velas)
    print(lechuga)
    print(huevo)

    print(velas > lechuga)
    print(velas < lechuga)
    print(huevo == lechuga)
