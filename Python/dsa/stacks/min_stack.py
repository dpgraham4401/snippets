"""Implement a minimum stack that meets the interface below.

It's a stack that keeps a reference to the minimum value in the stack.
"""

from typing import Protocol


class MinStack(Protocol):
    def __init__(self) -> None: ...

    def push(self, val: int) -> None: ...

    def pop(self) -> None: ...

    def top(self) -> int: ...

    def get_min(self) -> int: ...


class MyMinStack:
    """Alright, lets break this down.

    The Problem:
        We don't want to have to loop through and find the minimum value
        everytime there's a change to the stack. That would be expensive.

    The Solution:
        Maintain two stacks, one with the actual values, another
        (with an equal number of values at any given time) that contains
        the minimum value when each value was added to the stack.
        That way, if the minimum value is popped, we have the previous
        minimum that corresponds to the previous state of the stack
        (When there was one less value).
    """

    def __init__(self) -> None:
        self.stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1]) if self.min_stack else val
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]
