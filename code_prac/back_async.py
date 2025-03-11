import asyncio

async def periodic_task(interval):
    while True:
        print("Running periodic task...")
        await asyncio.sleep(interval)

async def main():
    # Run the periodic task and a one-time task
    periodic = asyncio.create_task(periodic_task(2))
    print("Main task running...")
    await asyncio.sleep(10)  # Simulating main work
    periodic.cancel()  # Cancel the periodic task
    print("Main task completed")

asyncio.run(main())
