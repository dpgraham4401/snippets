"""Example async HTTP client that uses JSON Placeholder.

https://jsonplaceholder.typicode.com/
"""
import random
from dataclasses import dataclass

from httpx import AsyncClient


@dataclass
class ToDo:
    """To Do item from json placeholder."""

    userId: int
    id: int
    title: str
    completed: bool


class Client:
    """HTTP Client for json placeholder."""

    def __init__(self) -> None:
        """Initialize the client with a session."""
        self.client: AsyncClient = AsyncClient()
        self.rand_int = random.randint(1, 1000)

    async def get_todos(self) -> list[ToDo]:
        """Get all ToDos from json placeholder."""
        response = await self.client.get(f"https://jsonplaceholder.typicode.com/todos/?_delay=2000&foo={self.rand_int}")
        response.raise_for_status()
        return [ToDo(**todo) for todo in response.json()]

    async def get_todo(self, todo_id: int) -> ToDo:
        """Get a single To Do from json placeholder."""
        response = await self.client.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}/?_delay=2000&foo={self.rand_int}")
        response.raise_for_status()
        return ToDo(**response.json())


