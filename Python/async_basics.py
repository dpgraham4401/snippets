"""
From the docs: https://docs.python.org/3/library/asyncio.html

asyncio is a library, part of the std lib, to write concurrent code using the async/await syntax.
asyncio provides a set of high-level APIs to:
    run Python coroutines concurrently and have full control over their execution;
    perform network IO and IPC;
    control subprocesses;
    distribute tasks via queues;
    ...
It also provides low-level APIs for library/framework developers
"""

import asyncio
import random

import requests

census_key = "a88b50af47f987e2e4f7b8a8178e0071fa06d360"
pop_2021 = f"https://api.census.gov/data/2021/pep/population?get=POP_2021&for=us:*&key={census_key}"
pop_2019 = f"https://api.census.gov/data/2019/pep/population?get=POP&for=us:*&key={census_key}"
pop_2017 = f"https://api.census.gov/data/2017/pep/population?get=POP&for=us:*&key={census_key}"


async def example_using_executor():
    """
    This seems to be the most simple and straight forward way to do something
    like execute synchronous
    code (such as the request library) inside an async function (using async/await syntax)
    """
    loop = asyncio.get_event_loop()  # 'grab a handle for event loop'
    future1 = loop.run_in_executor(None, requests.get, pop_2021)  # run in the said event loop
    future2 = loop.run_in_executor(
        None, requests.get, pop_2019
    )  # requests.get is our function to execute,
    future3 = loop.run_in_executor(
        None, requests.get, pop_2017
    )  # pop_* is an arg to pass to the function

    response1 = await future1
    response2 = await future2
    response3 = await future3
    print("2021 US population", response1.json()[1][0])
    print("2019 US population", response2.json()[1][0])
    print("2017 US population", response3.json()[1][0])


async def io_bound_task(i):
    print(f"start:   {i}")
    sleep_time = random.randint(0, 5)
    await asyncio.sleep(sleep_time)
    print(f"end:     {i}")
    return i


async def run_multiple_tasks():
    """
    Remember: Concurrency is a broad term that covers asynchronous and multiprocessor/parallelism

    To help remember asynchronous vs parallelism, asynchronous is single threaded,
    only one co-routine canocupy the threads 'focus' at a given time.
    parallel programming uses multiple threads, each task is running independently
    pretty straight forward :)
    """
    my_results = []
    # If we'd like to start a number of tasks and process them as completed,
    # we should use the following
    for f in asyncio.as_completed([io_bound_task(i) for i in range(1, 6)]):
        my_results.append(await f)
    print("my results: ", my_results)  # we don't really have any guarantees on start or stop order

    # we could use 'await' in list comp to store the results (kinda inception-y)
    # foo = [await f for f in asyncio.as_completed([io_bound_task(i) for i in my_task_ids])]


def main():
    # We can run multiple async tasks from a synchronous function like so
    print("Starting the main (synchronous) function")
    asyncio.run(run_multiple_tasks())
    print("End the main (synchronous) function")


if __name__ == "__main__":
    # asyncio.run(example_using_executor())
    main()
