"""Chapter 4. concurrent web requests.

In this chapter, we're learning about how to make concurrent web
requests using asyncio and the aiohttp library. During the process, we talk about
async context managers.
"""
import asyncio
from random import random

import aiohttp

from async_python.async_py.utils import timed


@timed
async def main():
    """Make concurrent web requests."""

    async with aiohttp.ClientSession() as session:
        urls = [f"https://jsonplaceholder.typicode.com/todos/?_delay=2000&foo={x}" for x in range(10)]
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        print(responses)

if __name__ == "__main__":
    asyncio.run(main())