# Lambda functions
# python implementation of anonymous functions. Anytime that a lambda function could be used, a regular function
# could be used instead. The power of lambda function comes from readability.
# I'm not crazy about the 'lambda' syntax, it's controversial anyway.
from typing import Callable, TypedDict, Literal


# In Python, functions are first class citizens -> they're objects.
# If we have a function that accepts a function (Callable).
def apply_operation(x: int, fn: Callable):
    return fn(x)


# we could define a new function when calling.
def square(x: int | float):
    """Returns a number squared"""
    # This takes up multiple lines, and we need to find a place for it, and the logic is defined elsewhere
    return x * x


# or we could define the logic inline if it's more readable
result = apply_operation(2, lambda y: y * y)
print(result)  # all the logic was neatly defined in one place.


# great places to use lambda functions are the map and filter functions.
# Take the below example data
class Grocery(TypedDict):
    name: str
    category: Literal["dairy", "produce", "meat"]
    price: float


grocery_list: list[Grocery] = [
    {"name": "milk", "category": "dairy", "price": 1.32},
    {"name": "cheese", "category": "dairy", "price": 4.69},
    {"name": "turkey", "category": "meat", "price": 8.99},
]

# The filter functions accepts a function and an iterator. It returns new iterator with the filter applied
# now instead of defining a separate function -> it's clear we just need meat items from the grocery list
meat_groceries = list(filter(lambda x: x["category"] == "meat", grocery_list))
print(meat_groceries)

# the map function has a similar signature, returns a new iterator but with the lambda fn applied to each element
discounted_list = list(map(lambda x: {**x, "price": x["price"] * 0.8}, grocery_list))
print(discounted_list)

# We can define a lambda function to inline logic for sorting, which can be useful if you need to sort something
# based on an attribute or outside the scope of the sort fn default behavior.
ids = ["id1", "id5", "id3", "id2", "id4"]

sorted_ids = sorted(ids, key=lambda x: int(x[2:]))
print(f"unsorted Ids: {ids}")
print(f"sorted Ids: {sorted_ids}")
