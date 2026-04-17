from app.adaptador import FakeNotificationService, InMemoryOrderRepository
from app.casos_de_uso import CreateOrderUseCase


def test_create_order():
    repo = InMemoryOrderRepository()
    notifier = FakeNotificationService()

    use_case = CreateOrderUseCase(repo, notifier)

    use_case.execute(user_id=1, total=100)

    assert len(repo.orders) == 1
