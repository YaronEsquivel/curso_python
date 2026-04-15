import asyncio

from .cpuBond import main_pool, main_pool_less
from .httpxClient import fetch_async
from .syncClient import fetch_sync

if __name__ == "__main__":
    fetch_sync()
    asyncio.run(fetch_async())
    main_pool()
    main_pool_less()
