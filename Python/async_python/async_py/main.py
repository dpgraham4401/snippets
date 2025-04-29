import asyncio
from asyncio import Task, create_task, gather

import uvloop
from async_py.client import Client, ToDo
from async_py.utils import timed


@timed
async def run_placeholder_import() -> None:
    """Get all ToDos from json placeholder.

    This currently does not operate as expected. The total run time is still a
    cumulative of the long-running calls, instead of just their longest call.
    """
    client = Client()
    todos: Task[list[ToDo]] = create_task(client.get_todos())
    todo_1: Task[ToDo] = create_task(client.get_todo(1))

    # tasks are scheduled to run as soon as possible, which is usually when the f
    # irst await is encountered Even though we've created the task,
    # additional statements before our first await will run before the task is added
    # to the event loop. This is why we see the print statements before the tasks are completed.
    print("Before await")

    # This will run ~2 seconds, instead of the sum (~4 seconds)
    await todos
    await todo_1
    # instead of using gather, we could await each task individually: await todos; await todo_1
    print(todos)
    print(todo_1)


def main() -> None:
    """Our normal, synchronous starting point for our programs."""
    uvloop.install()
    asyncio.run(run_placeholder_import())


if __name__ == "__main__":
    main()
