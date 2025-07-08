import cython

def cy_sum_squares(int n) -> cython.long:
    total: cython.long = 0
    i: cython.int
    for i in range(1, n + 1):
        total += i * i
    return total

