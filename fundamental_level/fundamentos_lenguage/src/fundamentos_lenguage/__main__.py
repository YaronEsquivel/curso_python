# __main__.py
import asyncio

from .services.service_json import main

if __name__ == "__main__":
    asyncio.run(main())
