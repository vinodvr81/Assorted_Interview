import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        data = await response.text()
        print(f"Fetched data from {url} with status {response.status}")
        return data

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)
        print("All tasks completed")

asyncio.run(main())