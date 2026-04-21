class ProductName:
    name: str

    def __init__(self, name):
        if not name.strip():
            raise ValueError("El nombre no puede ser vacio")
        if len(name) > 30:
            raise ValueError("El nombre es demasiado largo")
        self.name = name

    def __str__(self):
        return self.name
