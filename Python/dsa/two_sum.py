"""
Given a list of integers, return the indices of two numbers that add to the target value.
The array is not guaranteed to be sorted, every solution will have exactly one solution.
"""


def two_sums(nums: list[int], target) -> tuple[int, int]:
    diffs: dict[int, int] = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in diffs:
            return diffs[diff], i
        diffs[num] = i
    err_msg = "No solution found"
    raise ValueError(err_msg)


nums = [3, 4, 5, 6]
target = 9
print(two_sums(nums, target))
