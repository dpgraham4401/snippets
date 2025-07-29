"""*args, **kwargs, and the meaning of the '*'

args and kwargs (as often written and referred to) are an element of Python as a dynamic language
*args and **kwargs allow you to pass multiple arguments or keyword arguments to a function
This is easy in a dynamic language like python, it's not possible in some languages.
"""

# Say we have this dict
denominations = {
    "washington": 1,
    "lincoln": 5,
    "jackson": 20,
    "grant": 50,
    "franklin": 100,
}


def print_bill(name):
    print(f"{name}: {denominations[name]}")


# instead of just allowing a finite set of arguments like so
def get_one_denomination(name: str) -> None:
    print_bill(name)


get_one_denomination("jackson")


# we could allow as many names as needed to be passed
# note: args is just a common name, but the parameter could be named anything.
# the unpacking operator ('*') is what's important
def get_denominations(*args):
    """This flexibility is one of the great advantage of working with a dynamic lang"""
    print(type(args))
    for name in args:
        print_bill(name)


# args get passed as a tuple. Remember tuples are immutable
get_denominations("jackson", "washington", "franklin")


# the kwargs parameter is stored as a dict
def display_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")


# keyword args are passed as key=value pairs
display_kwargs(foo="bar", bar="foo")

# We can use '*' to denote parameters as keyword only arguments
# The order matters as well, we can't have optional (ones with default values) before kwargs without
# This 
def export_data(data: list, *, format: str, key1: int = 1, key2: int = 2):
    """
    Here, 
    1. 'data' arg is mandatory, 
    2. 'format' is mandatory as a keyword arg
    3. The 'keys' are optional but only as keyword args

    This keeps our function call very readable, like so.
    I know what data is being exported, and the format of the output
    export_data(my_data, format="CSV")
    """
