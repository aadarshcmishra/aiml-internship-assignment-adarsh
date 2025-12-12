import time
import asyncio

# --- Synchronous Implementation ---
def sync_task(delay, name):
    print(f"Sync Task {name} starting...")
    time.sleep(delay)  # Blocking delay
    print(f"Sync Task {name} finished.")
def run_sync():
    start = time.time()
    sync_task(2, "A")
    sync_task(2, "B")
    end = time.time()
    print(f"Total Sync Time: {end - start:.2f} seconds\n")
print("--- Running Synchronous ---")
run_sync()
