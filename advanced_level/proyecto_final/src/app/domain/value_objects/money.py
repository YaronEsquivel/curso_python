class Money:
    divisa: str
    cantidad: int

    def __init__(self, cantidad, divisa):
        if cantidad < 0:
            raise ValueError("No se ingreso una cantidad valida")
        if not divisa.strip():
            raise ValueError("Ingresa una divisa")
        self.cantidad = cantidad
        self.divisa = divisa
