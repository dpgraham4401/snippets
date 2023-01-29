import asyncio
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


if __name__ == "__main__":
    asyncio.run(example_using_executor())
