# __main__.py
import asyncio

from .services.transform_input_to_otuput_service import main

if __name__ == "__main__":
    asyncio.run(main())
