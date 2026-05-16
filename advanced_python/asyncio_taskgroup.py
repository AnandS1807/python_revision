import asyncio
import time

async def worker(name, duration):
  print(f"worker {name} ran for {duration} seconds")
  await asyncio.sleep(duration)
  print(f"worker {name} completed")  