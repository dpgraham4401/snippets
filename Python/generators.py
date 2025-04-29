# Generators
# from the docs Python.org docs:
#   Generator functions allow you to declare a function that behaves like an
#   iterator, i.e. it can be used in a for loop
#
# A generator yields a stream of data, one value/object at a time

# we declare generators just like regular function, except, we use the `yield`
# keyword in place of the `return`
# The yield keyword tells python to 'pause the execution,
# save state, and resume from the same state when required'

# From the docs:
#   The performance improvement from the use of generators is the result of
#   the lazy (on demand) generation of values, which translates to lower memory usage.
#   Furthermore, we do not need to wait until all the elements have been generated before we
#   start to use them. This is similar to the benefits provided by iterators,
#   but the generator makes building iterators easy.

# a simple example
def even_positive_nums(n: int):
    """return positive even numbers greater than or equal to arg"""
    current_value = 2
    while current_value <= n:
        yield current_value
        current_value += 2


# now we can iterate over the values 'yielded' by the generator
for i in even_positive_nums(7):
    print(f"{i},", end=" ")  # prints -> 2, 4, 6,
print("\n")

# fun note: the range() function (in python3) is a generator.
# In python2, xrange() was a generator and range() was not.
