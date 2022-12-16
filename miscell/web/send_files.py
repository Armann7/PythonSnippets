import asyncio

from pathlib import Path

import aiohttp


async def send_files(endpoint: str, files: list):
    for file in files:
        async with aiohttp.ClientSession() as session:
            f = open(file, "rb")
            async with session.put(endpoint, data=f, ssl=False) as resp:
                print(await resp.text())
            f.close()

if __name__ == "__main__":
    files = list(Path(".").glob("files/*"))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_files("http://localhost:8080/upload", files))
    loop.close()
