import asyncio
import logging

from pathlib import Path

import aiohttp

async def on_request_start(session, trace_config_ctx, params):
    print("Starting request")


async def send_files(endpoint: str, files: list):
    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_start.append(on_request_start)
    async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
        data = aiohttp.FormData()
        for index, file in enumerate(files):
            if len(files) == 1:
                index = ""
            data.add_field(f'file{index}', open(file, "rb"), filename=file.name)
            data.add_field(name='body', value=f'This is file {file.name}')

        async with session.post(endpoint, data=data) as resp:
            print(await resp.text())


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    files = list(Path(".").glob("files/*"))

    asyncio.run(send_files("http://localhost:9980/upload", files))
