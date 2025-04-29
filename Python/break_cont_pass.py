# the break, continue, and pass keywords

# pass is simple enough, it means "don't do anything." no operations.


class YouTriedToAccessAKeyThatDoesNotExistsError(KeyError):
    """A custom version of our error for readability (LOL)."""


def do_nothing():
    """We can use it in a function"""
    # Pretty straightforward


# lastly, it may be useful in control flows
if __package__ == "yo_moma":
    pass

# `break` and `continue` are most useful in control flow
alphabet = "abcdefg"


def print_line():
    print("\n" + "-" * 20)
    return


# when you see `break`, think "break out of the current loop"
print_line()
print("BREAK")
for letter in alphabet:
    if letter == "d":
        # This will stop the loop, so we will not iterate past "d" in this example.
        print("\nAww freak out!")
        break  # This will break out of the nearest loop (for or while)
    print(letter, end=" ")
print_line()

# when you see continue, just think "continue to next iteration"
print("CONTINUE")
for letter in alphabet:
    if letter == "d":
        print("\nnote: d is missing")
        continue
    print(letter, end=" ")
print_line()
