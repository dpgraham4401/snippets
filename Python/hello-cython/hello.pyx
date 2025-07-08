import cython

def say_hello(name: str) -> str:
    return f"Hello {name}"

@cython.boundscheck(False)
def cy_sum_squares(int n):
    cdef long long total = 0
    cdef int i
    for i in range(1, n + 1):
        total += i * i
    return total
