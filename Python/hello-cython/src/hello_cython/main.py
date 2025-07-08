import time
import numpy as np
from hello_cython.hello import cy_sum_squares
from hello_cython.convolve import naive_convolve

def py_sum_squares(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def main():
    n = 100_000_000
    start = time.time()
    py_sum_squares(n)
    print("Python:", time.time() - start)  # ~7.01479 seconds
    start = time.time()
    cy_sum_squares(n)
    print("Cython:", time.time() - start)  # ~0.0240 seconds

    # Example usage of naive_convolve
    arr = np.arange(9, dtype=np.float64).reshape(3, 3)
    kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float64)
    result = naive_convolve(arr, kernel)
    print("Convolution result:\n", result)

if __name__ == "__main__":
    main()
