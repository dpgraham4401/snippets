"""Refresher on using numpy for mathematical operations.

Numpy an optimized, widely adopted, library and is generally
considered the standard for computation in Python.
"""

import numpy as np

# Unlike python lists, numpy arrays are homogeneous.
simple_array = np.array([98, 37, 19, 5, 58])
print(f"{simple_array}")

# by default, numpy will convert the array to a base type
my_string_array = np.array(["a", 1, 3, "foo"])
print(f"{my_string_array=}")

# unlike lists, slicing a numpy array returns a 'view' of the original instead of a new list
my_view = simple_array[:2]
print(f"{my_view=}")

# inspecting an array
print(f"{my_view.ndim=}")  # The number of dimensions
print(f"{my_view.shape=}")  # The shape of the array
print(f"{my_view.dtype=}")  # The data type of the array
print(f"{my_view.size=}")  # The number of elements in the array

# creating an empty array
np.zeros((10, 2))

# sorting
arr = np.sort(simple_array)

# Adding a dimension
row_vector = simple_array[np.newaxis, :]
# or use expand_dims
col_vector = np.expand_dims(simple_array, axis=1)  # --> 5 rows, 1 column

# Operations
# Element-wise operations
arr = np.array([1, 2, 3])
arr * 2  # [2, 4, 6]
arr + 2  # [3, 4, 5]
arr_min, arr_max = arr.min(), arr.max()

# Crating a 2D array
data = np.array([[1, 2], [3, 4], [5, 6]])
print(f"{data=}")
print(f"{data[0]=}")  # first row
print(f"{data[0][1]=}")  # seconds element (column) of the first row
print(f"{data[0:2]=}")  # select rows starting at 0 up to (but not including) the 2nd row
