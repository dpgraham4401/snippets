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
    # note: if we don't await our tasks, they will likely not be executed because the program will exit and the event
    # loop will be closed before they complete.

    # This will run ~2 seconds, instead of the sum (~4 seconds)
    await todos; await todo_1
    # instead of using gather, we could await each task individually: await todos; await todo_1
    print(todos)
    print(todo_1)


def main() -> None:
    """Our normal, synchronous starting point for our programs."""
    uvloop.install()
    asyncio.run(run_placeholder_import())


if __name__ == "__main__":
    main()
