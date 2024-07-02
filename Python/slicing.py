# List slicing
# a way of access objects and ranges of objects from a list

foo = [0, 1, 2, 3, 4, 5, 6, 7]

# Get an individual element.
print(foo[3])  # -> get the fourth element (remember, list start at 0)

# We can use the ":" operator to indicate 'the rest of'

# read: start at index -3 and get the rest to the right
print(foo[-3:])  # -> [5, 6, 7]

# read: get everything to the left of index -3
print(foo[:-3])  # -> [0, 1, 2, 3, 4]

# Getting a range (it's important to remember, the right side of : is NON_INCLUSIVE
print(foo[1:4])  # -> [1, 2, 3]

# We can also use ":" to modify a list in place
bar = [1, 2, 3]
print(hex(id(bar)), "original mem address")  # -> 0x1047d9040
bar = [4, 5, 6]
print(hex(id(bar)), "new address, normal assignment")  # -> 0x104823700
bar[:] = [7, 8, 9]
print(hex(id(bar)), "address after [:]")  # -> 0x104823700

# The [:] will return a copy, not a reference
baz = bar[:]
print("baz == bar", baz == bar)  # -> True
print("baz is bar", baz is bar)  # -> False

# Lastly, a 'Stride' can be used to set the step increment
print(foo[0:7:2])  # -> [0, 2, 4, 6]
# starting at index 0, going to index 7, get every other element (2)
