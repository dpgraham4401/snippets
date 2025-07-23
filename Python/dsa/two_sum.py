"""
Given a list of integers, return the indices of two numbers that add to the target value.
The array is not guaranteed to be sorted, every solution will have exactly one solution.
"""

def two_sums(nums: list[int], target) -> tuple[int, int]:
    map: dict = {}
    for i, val in enumerate(nums):
        diff = target - val
        if diff in map:
            return (map[diff], i)
        map[val] = i
    raise ValueError("No two sum solution found")


nums = [3,4,5,6]
target = 7
print(two_sums(nums, target))
