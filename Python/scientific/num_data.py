"""1.3. NumPy: creating and manipulating numerical data

See Also:
    https://lectures.scientific-python.org/intro/numpy/index.html
"""

import numpy as np

arr = np.array([1, 2, 3], dtype=np.float64)

even_arr = np.arange(0, 20, 2)
off_backwards_arr = np.arange(21, 0, -2)

# Create a 2D array
simple_matrix = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])
matrix_1 = np.arange(0, 20).reshape(4, 5)
matrix_2 = np.linspace(0, 20, 20).reshape(4, 5)

# Matrix dot multiplication
print(matrix_2 * matrix_1)



