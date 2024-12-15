# More Asyncio Python

Really setting my mind to learn async because I need it for work now.
The polls app example was more about using aiohttp

## Learning summary

asyncio revolves around a couple objects:

- `coroutines`: essentially just a function that can work asynchronously and created with `async def`.
    - if you call a coroutine directly, it will not be put on the "event loop".
- `tasks`: A coroutine wrapper, that allows us to schedule a coroutine to run on the event loop.
    - Tasks inherit from coroutines.
- `event loop`: The main loop that runs all the coroutines.
    - The event loop is a singleton, and you can get the current event loop with `asyncio.get_event_loop()`.
    - There are alternative implementations of the event loop, like `uvloop`.