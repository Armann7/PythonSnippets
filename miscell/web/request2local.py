import aiohttp
import asyncio
import ssl


async def main():
    url = "https://core-s-dnifi02.gk.rosatom.local/www/store/common/реадме.txt"

    # ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
    # conn = aiohttp.TCPConnector(ssl=ssl_context)

    timeout = aiohttp.ClientTimeout(total=30)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=timeout) as response:
            if response.status == 200:
                content = await response.read()
                print(content.decode("utf-8"))
    await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(main())
