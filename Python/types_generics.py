"""Python Generics.

Generics allow us to define types that can be anything that meets the constraints we set (my words).
Some of this is Python typing, I don't see it used often in the wild (11/2024).

This file use generics that are only available in Python 3.12+.
"""

from collections.abc import Callable
from typing import TypeVar


# Generics are a way to make type annotations more flexible.
# The "preferred" way to use generics by annotating a function or class with
# square brackets before the parameter list.
def first_item[T](items: list[T]) -> T:
    """The funct_name[T](param: type[T]) -> type[T] syntax was introduced in Python3.12."""
    return items[0]


# If we need to use the generic type in multiple places, we can define a TypeVar.
# This TypeVar is equivalent to the generic type T in the above example. It can be anything.
# note: the string 'MyGeneric' must match the variable name (why? I don't know)
MyGeneric = TypeVar("MyGeneric")

# We can add constraints to our generic types, which is particularly useful
# when working with classes/interfaces(ABCs). Here are some example classes


class Animal:
    def __init__(self, name: str = "Animal", age: int = 1):
        self.name = name
        self.age = age

    def speak(self) -> str:
        return "Im an animal"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof"


class Bulldog(Dog):
    def speak(self) -> str:
        return "Woof, woof"


class GermanShepherd(Dog):
    def speak(self) -> str:
        return "Woof, woof"


# and some instances of those classes
my_dog = Dog(name="spud", age=1)
hund = GermanShepherd(name="hund", age=3)
my_bulldog = Bulldog(name="churchill", age=7)
my_cat = Cat(name="fluffy", age=3)
greendale_human = Animal(name="Jeff Winger", age=40)

# We can use the bound parameter to specify a generic type that is accepts a class,
# or subclass of that class
Canine = TypeVar("Canine", bound=Dog)  # a dog or any subclass of Dog


def is_puppy(dog: Canine) -> bool:
    """A function that only accepts a Dog or subclass of Dog."""
    return dog.age < 2


def pet_dog(dog: Canine) -> None:
    """A function that only accepts a Dog or subclass of Dog."""
    print(f"Good dog, {dog.name}!")


is_puppy(my_dog)  # -> true: OK because my_dog is a Dog
is_puppy(my_bulldog)  # false: OK because my_bulldog is a Bulldog, a subclass of Dog
# is_puppy(my_cat)  # Runs but -> mypy complains
# (Expected type 'Puppy ≤: Dog', got 'Cat' instead (mypy))


def is_old_puppy[Doggo: Dog](dog: Doggo) -> bool:
    """We can define the generic type inline if we don't need the reusability of TypeVar."""
    return dog.age > 5


is_old_puppy(my_dog)  # -> false: OK because my_dog is a Dog
is_old_puppy(my_bulldog)  # true: OK because my_bulldog is a Bulldog, a subclass of Dog
# is_old_puppy(my_cat)  # Runs but -> mypy complains (Expected type 'Doggo ≤: Dog',
# got 'Cat' instead  (mypy))


class Box[G]:
    """Classes can also have generic types. This box that can contain anything."""

    def __init__(self, content: G):
        self.content = content


box_of_abandoned_puppies = Box(my_dog)
box_of_abandoned_cats = Box(my_cat)
pet_dog(box_of_abandoned_puppies.content)  # -> Good dog, spud!
# pet_dog(box_of_abandoned_cats.content)  # -> Runs but mypy complains:
# (Expected type 'Canine ≤: Dog', got 'Cat' instead)


# We can also apply constraints to the generic type of class, just like functions
class BoxOfMyFavoriteDogTypes[Doggo: (GermanShepherd, Bulldog)](Box[Doggo]):
    """A box that can only contain German Shepherds or BullDogs of Dog."""


# another example of generic with constraints
def get_my_dog_name[D: (Bulldog, GermanShepherd)](dog: D) -> str:
    """A function that only accepts a Bulldog or German Shepherd."""
    return dog.name


# box_of_my_dogs = BoxOfMyFavoriteDogTypes(my_dog) (mypy no like)
box_of_my_dogs = BoxOfMyFavoriteDogTypes(my_bulldog)

##################### NOTE #####################
# I can get by, 99% of the time with the above usage. The below deals more with the crossroads
# of inheritance and generics.

### Invariant, Covariant and Contravariant types ###
# Some of the important terms to understand regarding inheritance + generics:
# - covariant: a type that can be converted to a more specific type
# (e.e., a Cat can be used as an Animal)
# - contravariant: a type that can be converted to a more general type
# (e.g., an Animal can be used as a Cat)
# - invariant: a type that must be the exact type
# (e.g., a Cat must be a Cat, Dog or animal is not allowed)
# https://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science)
# By default, Python generics are invariant!!!

# Example from Ruff docs:
# list[Dog] accepts only list[Dog] , not list[Animal] (superclass) or list[Bulldog] (subclass)


####### Other New type features in Python 3.12+ #######

# we can now use the 'type' function to create type variables (called type aliases)
type Graph = list[
    Point
]  # type aliases are evaluated lazily, they can be used before they are defined (how cool!)
type Point = tuple[int, int]
data_point: Point = (1, 2)

# A new way to declare ParamSpecs, which are used to represent a function's parameters.
# They are useful with decorators, and functions that accept/return functions as input/output.
# https://docs.python.org/3/library/typing.html#typing.ParamSpec
type NameGetterParamSpec[**P] = Callable[P, str]


def my_decorator(func: NameGetterParamSpec[int]) -> NameGetterParamSpec[int]:
    return func
