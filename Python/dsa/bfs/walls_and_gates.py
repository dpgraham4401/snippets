"""'Walls and Gates', AKA 'Islands and Treasures'

A common BFS algorithm problem.

You are given an M x N 2D grid initialized with these three possible values:
    * -1 - A water cell that can not be traversed.
    * 0 - A treasure chest.
    * INF - A land cell that can be traversed.
      We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest.
If a land cell cannot reach a treasure chest, then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.
"""

intput = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]


def map_islands_and_treasure(self, grid: list[list[int]]) -> None:
    pass
