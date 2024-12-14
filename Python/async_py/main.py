import asyncio
import time

from async_py.client import Client

async def run_placeholder_import() -> None:
    """Get all ToDos from json placeholder.

    This currently does not operate as expected. The total run time is still a
    cumulative of the long-running calls, instead of just their longest call.
    """
    start = time.time()
    client = Client()
    todos = await client.get_todos()
    end_todos = time.time()
    todo_1 = await client.get_todo(1)
    end_todo = time.time()
    print(todos)
    print(todo_1)
    end = time.time()
    print(f"Time to get all ToDos: {end_todos - start:.2f} seconds")
    print(f"Time to get a single ToDo: {end_todo - start:.2f} seconds")
    print(f"Time: {end - start:.2f} seconds")


def main() -> None:
    """Our normal, synchronous starting point for our programs."""
    asyncio.run(run_placeholder_import())


if __name__ == "__main__":
    main()
