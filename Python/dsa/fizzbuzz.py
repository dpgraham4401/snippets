"""
The classic, but stupid FizzBuzz interview question.
"""

def fizz_buzz(n: int) -> None:
    for i in range(1, n + 1):
        output: str = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output if output else i)

fizz_buzz(15)
