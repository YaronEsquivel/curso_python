from app.DTO import OrderDTO


class CreateOrderUseCase:
    def __init__(
        self,
        uow,
    ):
        self.uow = uow

    def execute(self, dto):
        with self.uow:
            order = OrderDTO(dto.user_id, dto.total)
            self.uow.orders.save(order)

            return order
