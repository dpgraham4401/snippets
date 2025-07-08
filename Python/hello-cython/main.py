import time
from hello import  cy_sum_squares


def py_sum_squares(n: int) -> int:
    """Calculate the sum of squares from 1 to n. The Python implementation."""
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def main():
    """Quick benchmark of Python v. Cython via sum-of-squares. The times are from my local machine."""
    n = 100_000_000

    start = time.time()
    py_sum_squares(n)
    print("Python:", time.time() - start)  # 6.637583494186401 seconds

    start = time.time()
    cy_sum_squares(n)
    print("Cython:", time.time() - start)  # 0.024001121520996094 seconds

if __name__ == "__main__":
    main()
