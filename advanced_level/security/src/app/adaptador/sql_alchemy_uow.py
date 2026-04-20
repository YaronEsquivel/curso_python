from app.adaptador import SqlAlchemyOrderRepository
from app.puerto import UnitOfWork


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()

        self.orders = SqlAlchemyOrderRepository(self.session)

        return self

    def __exit__(self, exc_type, exc, tb):
        if exc:
            self.session.rollback()
        else:
            self.session.commit()

        self.session.close()
