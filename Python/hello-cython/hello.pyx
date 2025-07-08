"""Using Cython.

Cython is a superset of Python (all valid Python is valid cython) that compiles to C extensions modules.
We gain speed by adding Cython package type hints to our pyx Python code, using C files, and generally finding
ways to release the GIL (Global Interpreter Lock) in Python.

There are two ways to use Cython in a .pyx file:
1. Pure Python type hints (PEP 484 style) from the `cython` module
2. Cython, using C type hints (using the `cdef` keyword)
"""
import cython

def cy_sum_squares(int n) -> cython.long:
    """We're using PEP hints, the comments show the Cython equivalent."""
    total: cython.long = 0  # cdef long total = 0
    i: cython.int  # cdef int i
    for i in range(1, n + 1):
        total += i * i
    return total
