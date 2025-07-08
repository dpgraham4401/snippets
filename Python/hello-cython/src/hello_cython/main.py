import time
from hello_cython.hello import cy_sum_squares

def py_sum_squares(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def main():
    n = 100_000_000
    start = time.time()
    py_sum_squares(n)
    print("Python:", time.time() - start)
    start = time.time()
    cy_sum_squares(n)
    print("Cython:", time.time() - start)

if __name__ == "__main__":
    main()

