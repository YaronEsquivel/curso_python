import logging

from .config.db import engine, seed_data
from .models.Base import Base
from .service.consumeDB import menu, query_data

logger = logging.getLogger(__name__)


def setup_loggin():
    logging.basicConfig(level=logging.INFO)


def init_bd():
    Base.metadata.create_all(engine)


def main():
    setup_loggin()
    init_bd()

    logger.info("Inicializando proyecto")

    data = query_data()
    if not data:
        seed_data()
    menu()


if __name__ == "__main__":
    main()
