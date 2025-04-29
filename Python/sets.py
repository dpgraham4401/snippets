list1 = ["apple", "banana", "cherry"]
list2 = ["apple", "banana", "date"]

# notice that 'date' is not included in the diff since
#  we're substracting list2 from list1
diff = set(list1) - set(list2)

# If we do not cast diff as a list, it will be a dict by default
print(list(diff))

# another way
diff2 = list(set(list1).difference(set(list2)))
print(diff2)

# sets can also be declared with the {} syntax (don't be confused, it's not a dict)
my_set = {"banana", "apple"}
print(my_set)  # results -> {'banana', 'apple'}
print(f"is set: {isinstance(my_set, set)}")
