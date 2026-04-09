# __main__.py
import asyncio

from .service.process_service import main

if __name__ == "__main__":
    asyncio.run(main())
