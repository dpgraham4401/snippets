list1 = ['apple', 'banana', 'cherry']
list2 = ['apple', 'banana', 'date']

# notice that 'date' is not included in the diff since 
#  we're substracting list2 from list1
diff = set(list1) - set(list2)

# If we do not cast diff as a list, it will be a dict by default
print(list(diff))

# another way
diff2 = list(set(list1).difference(set(list2)))
print(diff2)
