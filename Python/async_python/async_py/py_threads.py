"""Using Threads in Python to handle blocking work.

Even though Python has the GIL, multithreading is a great way to handle IO bound synchronous code,
for example using legacy popular HTTP libraries like requests.
Blocking IO releases the global interpreter lock, enabling the possibility of running IO
concurrently.

concurrent.futures pkg provides ThreadPoolExecutor, which will create and maintain a pool
of thread that we can submit work to.
"""

import asyncio
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import socket
import time

import requests


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


async def main():
    urls = ["https://www.example.com" for _ in range(1000)]
    start = time.time()

    ### Synchronous --> about 35 seconds (Dell Latitude)
    # results = [get_status_code(u) for u in urls]

    ### ThreadPoolExecutor --> about 5 seconds (same Dell Latitude)
    # with ThreadPoolExecutor() as pool:
    #     results = pool.map(get_status_code, urls)

    ### asyncio combined with threads --> about 5 seconds
    # this is just a nicer API that using the ThreadPoolExecutor
    tasks = [asyncio.to_thread(get_status_code, url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)

    end = time.time()
    print(f"finished request in {end - start:.4f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
