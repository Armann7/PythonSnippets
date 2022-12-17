import asyncio

from pathlib import Path

import aiohttp


async def send_files(endpoint: str, files: list):
    async with aiohttp.ClientSession() as session:
        # data = aiohttp.FormData()
        # for file in files:
        #     data.add_field('file', open(file, "rb"), filename=file.name)
        with aiohttp.MultipartWriter('mixed') as mpwriter:
            for file in files:
                with aiohttp.MultipartWriter('related') as subwriter:
                    # subwriter.append_payload(aiohttp.Payload(open(file, "rb")))
                    ...
            mpwriter.append_(subwriter)
        async with session.put(endpoint, data=mpwriter) as resp:
            print(await resp.text())

if __name__ == "__main__":
    files = list(Path(".").glob("files/*"))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_files("http://localhost:8080/upload/", files))
    loop.close()
