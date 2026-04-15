import asyncio
import time

import httpx

urls = ["https://example.com"] * 50

semaphore = asyncio.Semaphore(10)


async def fetch(client, url):
    async with semaphore:
        r = await client.get(url)
        return r.status_code


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, url) for url in urls]
        return await asyncio.gather(*tasks)


async def fetch_async():
    start = time.time()
    await main()
    print("tiempo de las 50 peticiones asincronas:", time.time() - start)
