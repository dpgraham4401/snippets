"""
Given a string, return whether it is a palindrome or not.
Palindromes ignore spaces and all non-alphanumeric characters 
(i.e., presence of one does not negate the palindrome)
"""

def is_palindrome(s: str) -> bool:
    """This is the simplest Python syntax, but it doesn't ignore alphanumeric characters."""
    reverse_string = s[::-1]
    if reverse_string == s:
        return True
    return False

def two_pointer_pal(s: str) -> bool:
    tokens = list(s)
    cleaned = ''.join(token for token in tokens if token.isalnum()).lower()
    i = 0
    n = len(cleaned) - 1
    while i < n:
        if cleaned[i] != cleaned[n]:
            return False
        i += 1
        n -= 1
    return True

def run(s: str):
    """Having fun with f-strings."""
    print(f"'{s}' is {"not " if not two_pointer_pal(s) else ""}a palindrome")

car = "racecar"
not_pal = "foobarbaz"
complex="Was it a car or a cat I saw?"

# run(car)
# run(not_pal)
run(complex)


