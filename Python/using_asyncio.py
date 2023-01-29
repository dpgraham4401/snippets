import asyncio
import random
import requests

census_key = 'a88b50af47f987e2e4f7b8a8178e0071fa06d360'
pop_2021 = f'https://api.census.gov/data/2021/pep/population?get=POP_2021&for=us:*&key={census_key}'
pop_2019 = f'https://api.census.gov/data/2019/pep/population?get=POP&for=us:*&key={census_key}'
pop_2017 = f'https://api.census.gov/data/2017/pep/population?get=POP&for=us:*&key={census_key}'


# urls = [pop_2021, pop_2019, pop_2017]

async def example_using_executor():
    """
    This seems to be the most simple and straight forward way to do something like execute synchronous
    code (such as the request library) inside an async function (using async/await syntax)
    """
    loop = asyncio.get_event_loop()  # 'grab a handle for event loop'
    future1 = loop.run_in_executor(None, requests.get, pop_2021)  # run in the said event loop
    future2 = loop.run_in_executor(None, requests.get, pop_2019)  # requests.get is our function to execute,
    future3 = loop.run_in_executor(None, requests.get, pop_2017)  # pop_* is an arg to pass to the function

    response1 = await future1
    response2 = await future2
    response3 = await future3
    print('2021 US population', response1.json()[1][0])
    print('2019 US population', response2.json()[1][0])
    print('2017 US population', response3.json()[1][0])


async def io_bound_task(i):
    print(f"start:   {i}")
    sleep_time = random.randint(0, 5)
    await asyncio.sleep(sleep_time)
    print(f"end:     {i}")
    return i


async def run_multiple_tasks():
    my_results = []
    # Import note, using 'async for' does not iterate and start a number of concurrent tasks
    # If we'd like to start a number of tasks and process them as completed, we should use the following
    for f in asyncio.as_completed([io_bound_task(i) for i in range(1, 6)]):
        my_results.append(await f)
    print('my results: ', my_results)  # we don't really have any guarantees on start or stop order

    # If we want to use list comp to store the results, we could await the results (kinda inception-y)
    # foo = [await f for f in asyncio.as_completed([io_bound_task(i) for i in my_task_ids])]


if __name__ == "__main__":
    # we can initiate our async functions with the asyncio.run function
    # asyncio.run(example_using_executor())
    asyncio.run(run_multiple_tasks())
