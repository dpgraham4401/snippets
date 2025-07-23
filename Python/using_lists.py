#!/bin/python
# using_lists.py


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    # def __repr__(self):
    #     return f'Person object named {self.name}'


def main():
    print("############################")
    print("List Comprehension")
    print("############################")
    # list comprehension is a way to create a new iterable (array, dict) in shorthand
    # the new iterable is usually derived from another

    # for example, say i have an array of Person object
    people = [Person("jim", 42), Person("bob", 21), Person("claire", 63)]

    # if we print that array, we get either the whatever the __repr__ method defines for those obj
    print("This is probably not useful:")
    print(people)
    print("\n")

    # If we needed an array of the string representation of these object,
    # we could use list comprehension
    people_str = [str(person) for person in people]
    print("An array of string representations of the objects is easier to deal with:")
    print(people_str)
    print("\n")

    # we can embed more complex logic in list comprehension as well such as
    # if statement
    people_str_filtered = [str(person) for person in people if str(person) == "jim"]
    number_array = [i for i in range(10) if i % 2 == 0]
    print("IF logic is kind of like filtering...")
    print("if elements == 'jim'")
    print(people_str_filtered)
    print("only even numbers")
    print(number_array)
    print("\n")

    # although this file is called list_comprehension, the same logic can be used for sets and dicts
    set_comp = {str(people[i]) for i in range(len(people))}
    dict_comp = {i: str(people[i]) for i in range(len(people))}
    print("Rets and dicts")
    print(set_comp)
    print(dict_comp)
    print("\n")


if __name__ == "__main__":
    main()
