import logging
import time

import httpx

from ..utils.constants import PATHS

logger = logging.getLogger(__name__)


async def consume(PATH):
    path = "Path erroneos"
    for i in range(3):
        try:
            if i == 2:
                path = PATH
            async with httpx.AsyncClient() as client:
                response = await client.get(path, timeout=3.0)
                logger.info(f"response: {response.json()}")
                if response.json():
                    await get_image(response.json()["message"])
                    break
        except Exception as e:
            handle_exception(e, i)


async def get_image(uri):
    OUTPUT_PATH = PATHS.get("OUTPUT_PATH")
    OUTPUT_PATH.mkdir(exist_ok=True)
    dog_image_path = OUTPUT_PATH / "dog_image.jpg"
    async with httpx.AsyncClient(timeout=5.0) as client:
        url = ""
        for i in range(3):
            try:
                if i == 2:
                    url = uri
                else:
                    url = f"{uri} bla bla bla"
                async with client.stream("GET", url) as response:
                    response.raise_for_status()

                    with dog_image_path.open("wb") as f:
                        async for chunk in response.aiter_bytes():
                            f.write(chunk)
                        logger.info("\nExitoso :)\n")
                        break
            except httpx.TimeoutException as e:
                handle_exception(e, i)

            except httpx.HTTPStatusError as e:
                handle_exception(e, i)

            except httpx.RequestError as e:
                handle_exception(e, i)


def handle_exception(e, i):
    logger.error(f"Hubo un error: {e}")
    if i < 2:
        logger.warning("reintentando...\n")
    else:
        logger.error("se lanzará una excepcion")
        raise
    time.sleep(2)
