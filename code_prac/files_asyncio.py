import asyncio
import aiofiles

async def process_file(filename):
    async with aiofiles.open(filename, mode='r') as file:
        async for line in file:
            await asyncio.sleep(0.1)
            print(f"Processed line: {line.strip()}")


async def main():
    await asyncio.gather(
        process_file("hist1.txt"),
        process_file("scan_log.txt")
    )

asyncio.run(main())