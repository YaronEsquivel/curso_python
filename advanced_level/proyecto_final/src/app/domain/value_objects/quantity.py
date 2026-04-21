class Quantity:
    value: int

    def __init__(self, value):
        if value < 0:
            raise ValueError("La cantidad debe ser mayor que 0")
        self.value = value
