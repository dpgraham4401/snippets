"""
Using Iterators.
Python iterators provide a way to traverse a container of elements and visit each.
Iterators provide a way to decouple the algorithm used to traverse the container from
the container itself. For example, we can iterate over a list, a sequence of bytes, file, any class
that implements the .__iter__() method and the .__next__() (or .__aiter__() and .__anext__() for async)

iterators allow us to stream data, meaning we process the data as it arrives instead of readin the
entire data into memory.
"""

import asyncio
from collections.abc import Iterator, Sequence
from random import randint

data1 = [1, 2, 3]
data2 = [10, 20, 30]

# zip takes two iterators, python lists fulfil the iterator protocol
zipped_data = zip(data1, data2, strict=True)
# for foo in zipped_data --> (1, 10), (2, 20), (3, 30)


class MyIterator:
    """This is a contrived example that could be replaced with the iter() and next() functions."""

    def __init__(self, seq: Sequence, stop: int = 5):
        self._seq = seq
        self._index = 0
        self._stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        """This is where the magic happens."""
        if self._index < len(self._seq):
            item = self._seq[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._index >= self._stop:
            raise StopAsyncIteration
        await asyncio.sleep(value := randint(1, 3))
        self._index += 1
        return value


my_iter = MyIterator(data1)

# for foo in my_iter:
#     print(foo)  # 1, 2, 3


"""
Generators.

Generators are a special kind of iterators.
A 'generator function' is the fn that uses the yield statement to return a 'generator iterator'
Generators are a great/easy way to make out program more memory efficient.
"""


def gen_func() -> Iterator:
    """Just that simple."""
    for item in data1:
        yield item


# for foo in gen_func():
#     print(foo)  # 1, 2, 3

"""We also have generator expressions, which functionally act similar to list comprehension"""

# one might think this returns a tuple, but it's actually a generator
gen_expression = (item for item in data1)
print(gen_expression)


"""Iterator constraints.
1. Iterators can only be iterated over once. Once consumed, it's exhausted.
2. You can’t reset an exhausted iterator to start iteration again.
3. There’s no .__previous__() method. You can only move forward through an iterator. You can’t move backward.
4. Because iterators only keep one item in memory at a time, you can’t know their length or number of items.
5. Iterators don’t allow indexing and slicing operations with the [] operator

These constraints emphasize that, half the point of using an iterator, are meant to ease keeping track of 
our place while traversing a container/collection.
"""

iter_constraints = iter(data1)

try:
    print(len(iter_constraints))
except TypeError:
    print("iterators do not implement methods to get their length")

for foo in iter_constraints:
    print(foo)

for foo in iter_constraints:
    print(foo)  # This will print nothing


"""Async iteration isn't that different. We just need a class that implements the __aiter__ and __anext__."""


async def main():
    another_iter = MyIterator(data1)
    async for item in another_iter:
        print(item)


asyncio.run(main())
