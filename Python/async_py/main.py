import asyncio
import time

from async_py.client import Client
from async_py.utils import timed


@timed
async def run_placeholder_import() -> None:
    """Get all ToDos from json placeholder.

    This currently does not operate as expected. The total run time is still a
    cumulative of the long-running calls, instead of just their longest call.
    """
    client = Client()
    todos = await client.get_todos()
    todo_1 = await client.get_todo(1)
    print(todos)
    print(todo_1)


def main() -> None:
    """Our normal, synchronous starting point for our programs."""
    asyncio.run(run_placeholder_import())


if __name__ == "__main__":
    main()
