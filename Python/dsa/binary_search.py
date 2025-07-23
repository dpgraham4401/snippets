"""
Given a list of distinct ascending integers, and a target value, implement a binary search to find
the index of the target value.
if the target does not exists, return -1
"""

def binary_search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)

    while l < r:
        m = l + ((r - l) // 2)
        if nums[m] < target:
            l = m + 1
        if nums[m] > target:
            r = m - 1
        if nums[m] == target:
            return m
    return -1

my_nums = [1, 2, 3, 5, 6, 8, 9]

print(binary_search(my_nums, 8))  # return index of 8
print(binary_search(my_nums, 7))  # non-existant --> return -1
