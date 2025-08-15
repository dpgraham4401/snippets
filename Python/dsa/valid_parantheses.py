"""
Given a string of brackets, check if it is valid.
A common technique is to use a stack, and a map of closing-opening brackets.
Loop over the string, for each open bracket, add it to the stack, for each closing, check if it matches the
last element in the stack, otherwise the paratheses are not balanced.
"""


def is_valid(s: str) -> bool:
    stack: list[str] = []
    bracket_map = {
        "}": "{",
        "]": "[",
        ")": "(",
    }
    for char in s:
        if char in bracket_map:
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0


brackets = "({{()}[]})"
bad_brackets = "({{(}[]})"
print(f"{brackets} is valid: ", is_valid(brackets))
print(f"{bad_brackets} is valid: ", is_valid(bad_brackets))
