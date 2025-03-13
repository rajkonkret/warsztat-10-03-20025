import asyncio
import time
import aiohttp


async def fetch(url, session, index):
    async with session.get(url, ssl=False) as response:
        text = await response.text()
        print(f"Text: {text}")
        return response.status


async def measure_aiohttp():
    url = 'https://api.nbp.pl/api/exchangerates/rates/A/EUR/'
    tasks = []

    overall_start_time = time.time()

    async with aiohttp.ClientSession() as session:
        for i in range(100):
            tasks.append(fetch(url, session, i + 1))

        statuses = await asyncio.gather(*tasks)

    overall_elapsed_time = time.time() - overall_start_time
    print(f"Overall time for request: {overall_elapsed_time:.4f} seconds")
    return statuses


asyncio.run(measure_aiohttp())
# Overall time for request: 0.2934 seconds
