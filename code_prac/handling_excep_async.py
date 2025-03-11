import asyncio

async def faulty_task():
    await asyncio.sleep(2)
    raise ValueError("An error occurred in the task")

async def main():
    task = asyncio.create_task(faulty_task())
    try:
        await task
    except ValueError as e:
        print(f"Caught exception: {e}")

asyncio.run(main())
