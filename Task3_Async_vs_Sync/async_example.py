import time
import asyncio
async def async_task(delay, name):
    print(f"Async Task {name} starting...")
    await asyncio.sleep(delay)  # Non-blocking delay
    print(f"Async Task {name} finished.")

async def run_async():
    start = time.time()
    # Run both tasks concurrently
    await asyncio.gather(async_task(2, "A"), async_task(2, "B"))
    end = time.time()
    print(f"Total Async Time: {end - start:.2f} seconds")
print("--- Running Asynchronous ---")
asyncio.run(run_async())
