"""Chapter 4. concurrent web requests.

In this chapter, we're learning about how to make concurrent web
requests using asyncio and the aiohttp library. During the process, we talk about
async context managers.
"""

import asyncio

import aiohttp
from aiohttp import ClientResponse

from async_python.async_py.utils import timed


async def fetch_with_gather() -> None:
    """Make X requests and use gather to wait for all of them.

    Good:
        - It's simple to use.
        - even though task execution order is non-deterministic,
        the results are returned in the order of the tasks.

    problems with asyncio.gather:
        - It waits for all tasks to complete before returning any results.
        - If one task fails, we have to wait for all the
        others to complete before we can see the error.
    """
    async with aiohttp.ClientSession() as session:
        urls = [
            f"https://jsonplaceholder.typicode.com/todos/?_delay=2000&foo={x}" for x in range(10)
        ]
        tasks = [session.get(url, raise_for_status=True) for url in urls]
        # gather returns a list of the completed results
        responses: list[ClientResponse] = await asyncio.gather(*tasks)

        # If an exception occurs, and we don't pass return_exceptions=True,
        # the exception will be raised.
        # responses: list[ClientResponse] = await asyncio.gather(*tasks, return_exceptions=True)
        print(responses)


async def fetch_with_create_task() -> None:
    """Make X requests and use create_task to wait for all of them.

    Good:
        - We can process the results as they come in.
        - If one task fails, we can see the error immediately.

    problems with asyncio.create_task:
        - We have to keep track of the tasks ourselves.
        - We have to await each task individually.
        - The API is clunky.
    """
    async with aiohttp.ClientSession() as session:
        urls = [
            f"https://jsonplaceholder.typicode.com/todos/?_delay=2000&foo={x}" for x in range(10)
        ]
        requests = [session.get(url, raise_for_status=True) for url in urls]

        tasks = []

        for request in requests:
            tasks.append(asyncio.create_task(request))

        for task in tasks:
            response = await task
            print(response)


async def fetch_with_as_completed() -> None:
    """Make X requests and use as_completed to wait for all of them.

    Good:
        - We can process the results as they come in.
        - If one task fails, we can decide how to handle it.
        - Better control over exceptions.
        - timeout parameter to cancel tasks.

    problems:
        - results come in as they complete, there's no guarantee of order.
        - if we want to cancel b/c an error, we need to
    """
    async with aiohttp.ClientSession() as session:
        urls = [
            f"https://jsonplaceholder.typicode.com/todos/{x}/?_delay=2000&foo={x}"
            for x in range(1, 10)
        ]
        fetchers = [session.get(url, raise_for_status=True) for url in urls]

        # as_completed returns an iterator that yields the results as they come in.
        for done_task in asyncio.as_completed(fetchers, timeout=5):
            # we can handle exceptions in a natural, pythonic way.
            try:
                response = await done_task
                print(response)
            except TimeoutError:
                print("Timed out")


async def fetch_with_wait() -> None:
    """Make X requests and use 'wait' to gain fine-grained control over the results.


    Good:
        - timeout support.
        - fine-grained control over completed and pending tasks.
        - we can decide how to handle exceptions.

    challenges:
        - more complex to use than gather or as_completed.
        - verbose.
    """
    async with aiohttp.ClientSession() as session:
        urls = [
            f"https://jsonplaceholder.typicode.com/todos/{x}/?_delay=2000&foo={x}"
            for x in range(1, 10)
        ]
        fetchers = [asyncio.create_task(session.get(url, raise_for_status=True)) for url in urls]

        # asyncio gives us couple options for when we see the first results (done, pending)
        done, pending = await asyncio.wait(fetchers, timeout=5, return_when=asyncio.FIRST_COMPLETED)
        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                print(done_task.exception())


@timed
async def main():
    """Make concurrent web requests."""

    # create_task is flexible, but it's more work to use.
    await fetch_with_create_task()

    # gather is easier to use, but it's less flexible.
    await fetch_with_gather()

    # as_completed is more flexible, but has some drawbacks as well.
    await fetch_with_as_completed()

    # wait is the most flexible, but it's also the most complex.
    await fetch_with_wait()


if __name__ == "__main__":
    asyncio.run(main())
