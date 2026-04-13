import asyncio
import logging

from .service.consume import consume


def setup_logging():
    logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    setup_logging()
    path = "https://dog.ceo/api/breeds/image/random"
    asyncio.run(main=consume(path))
