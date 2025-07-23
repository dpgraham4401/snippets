"""
Given a list of integers, return a boolean indicating whether there are any duplicates in the list.
"""

def has_duplicates(nums: list[int]) -> bool:
    seen  = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


no_dup = [1, 2, 3, 4, 5]
yes_dup = [1, 2, 3, 3, 4, 4]

print(has_duplicates(no_dup))  # False
print(has_duplicates(yes_dup))  # True