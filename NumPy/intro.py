'''

---> NumPy - NumPy (short for Numerical Python) is one of the most important Python libraries for scientific c->omputing and numerical operations.

---> It provides a fast and efficient way to work with:

    Numbers
    Arrays
    Matrices
    Mathematical functions
    Linear algebra
    Statistics
    Random number generation
    And much more

Think of NumPy as the foundation of the Python data science ecosystem. 
Libraries like Pandas, Matplotlib, SciPy, Scikit-learn, TensorFlow, PyTorch, and OpenCV either use NumPy directly or are built to work seamlessly with NumPy arrays.


---> NumPy arrays - A NumPy array is the main data structure provided by NumPy.

It is a collection of elements stored in contiguous memory, usually all of the same data type, allowing operations to be performed much faster than with Python lists.
Think of it as an upgraded version of a Python list designed specifically for numerical computations.

Characteristics of NumPy Arrays
1. Fixed Size - After creation, the size cannot be changed directly.
2. Same Data Type
3. Stored in Contiguous Memory - Instead of storing references to objects like Python lists, NumPy stores elements in a continuous block of memory.
4. Faster Computation
5. Supports Mathematical Operations

'''


import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr)
print()
print(arr*2)
print(type(arr)) # nd array - N dimesnional array

arr1 = np.array([1,2,3,4,5,6,7,8,9])
print(arr.dtype)
print(arr.nbytes)

