class Order:
    def __init__(self, user_id: int, total: float):
        if total <= 0:
            raise ValueError("Total inválido")

        self.user_id = user_id
        self.total = total
