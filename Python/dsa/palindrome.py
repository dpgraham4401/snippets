"""
Given a string, check if it is a palindrome.
A common technique is to use a stack, and a map of closing-opening brackets.
Loop over the string, for each open bracket, add it to the stack, for each closing, check if it matches the
last element in the stack, otherwise the paratheses are not balanced.
"""


def is_palindrome(s: str) -> bool:
    stack = []
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
                return False
        else:
            stack.append(char)
    return True


brackets = "({{()}[]})"
bad_brackets = "({{(}[]})"
print(is_palindrome(brackets))
print(is_palindrome(bad_brackets))
