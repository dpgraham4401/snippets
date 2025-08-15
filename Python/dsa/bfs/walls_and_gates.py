"""'Walls and Gates', AKA 'Islands and Treasures'

A common BFS algorithm problem.

You are given an M x N 2D grid initialized with these three possible values:
    * -1 - A water cell that cannot be traversed.
    * 0 - A treasure chest.
    * INF - A land cell that can be traversed.
      We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest.
If a land cell cannot reach a treasure chest, then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.
"""

from collections import deque

grid_input = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]

expected_output = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]

LAND = 2147483647
WATER = -1
CHEST = 0


def map_islands_and_treasure(grid: list[list[int]]) -> None:
    """Map out the number of moves to the nearest treasure chest.

    Instead of finding every piece of land, then for each piece of land find the closest chest,
    We're going to work backwards from the chests themselves.
    """
    ROWS, COLS = len(grid), len(grid[0])
    visited: set[tuple[int, int]] = set()
    q: deque[tuple] = deque()

    def visit_square(r: int, c: int) -> None:
        """Mark a room as visited and add it to the deque if the following criteria is met:

        1. It's not impassible (water)
        2. It's not out of bounds
        3. it hasn't already been visited
        """
        is_out_of_bounds: bool = r < 0 or r >= ROWS or c < 0 or c >= COLS
        if is_out_of_bounds:
            return
        is_water: bool = grid[r][c] == WATER
        has_been_visited = (r, c) in visited
        if is_water or has_been_visited:
            return
        visited.add((r, c))
        q.append((r, c))

    # The first step is to find the treasure chests
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == CHEST:
                q.append((r, c))
                visited.add((r, c))

    dist = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            grid[r][c] = dist
            visit_square(r + 1, c)
            visit_square(r - 1, c)
            visit_square(r, c + 1)
            visit_square(r, c - 1)
        dist += 1


map_islands_and_treasure(grid_input)

print(grid_input)
print(expected_output)
assert grid_input == expected_output
