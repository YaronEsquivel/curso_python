from app.adaptador.InMemoryOrderRepository import InMemoryOrderRepository
from app.adaptador.SQLAlchemyOrderRepository import SqlAlchemyOrderRepository
from app.models import OrderModel
from app.puerto import OrderRepository


def repository_contract(repo: OrderRepository):
    order = OrderModel(user_id=1, total=100)
    repo.save(order)


def test_inmemory_repo():
    repository_contract(InMemoryOrderRepository())


def test_sql_repo(session):
    repository_contract(SqlAlchemyOrderRepository(session))
