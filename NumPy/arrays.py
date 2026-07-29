'''

---> NumPy arrays - A NumPy array is the main data structure provided by NumPy.

It is a collection of elements stored in contiguous memory, usually all of the same data type, allowing operations to be performed much faster than with Python lists.
Think of it as an upgraded version of a Python list designed specifically for numerical computations.

Characteristics of NumPy Arrays
1. Fixed Size - After creation, the size cannot be changed directly.
2. Same Data Type
3. Stored in Contiguous Memory - Instead of storing references to objects like Python lists, NumPy stores elements in a continuous block of memory.
4. Faster Computation
5. Supports Mathematical Operations

---> Why NumPy arrays?

1. Faster Execution - NumPy arrays are implemented in C, making operations much faster than Python lists.
2. Less Memory Usage - NumPy stores data in a continuous block of memory, whereas Python lists store references to objects.
3. Mathematical Operations - You can perform operations on the entire array at once.
4. Supports Multi-dimensional Arrays - NumPy can easily create - 1D Arrays, 2D Arrays, 3D Arrays, n-Dimensional Arrays
5. Huge Collection of Built-in Functions

'''

# dtype (data type) = Keyword argument that tells NumPy what kind of values are stored in an array
#              Otherwise NumPy guesses the best data type based on your data
#              Manually setting dtype improves performance
#              & is more memory efficient (especially when working with large data sets)
# Unlike Python lists (which can hold mixed data types), 
# NumPy arrays are designed to store elements of a single data type. This allows NumPy to be faster and more memory-efficient.

# nbytes (total no of bytes) - tells you the total number of bytes occupied by all elements in the array.

# integer (int8, int16, int32, int64)
# float (float16, float32, float64)
# boolean (bool_) if _ not inlcuded, then that is a python boolen. anything thats non 0 will be True.
# string (str_, <U#) # the elmnts will be converted to str. it can be used for fixed length unicode str.
# object (object_)

# int8 = -128 to 127
# int16 = –32,768 to 32,767
# int32 = –2,147,483,648 to 2,147,483,647
# int64 = –9.22e18 to 9.22e18

# float16 = ~3-4 decimal digit precision
# float32 = ~7-8 decimal digit precision
# float64 = ~15-17 decimal digit precision

import numpy as np

array = np.array([1, 2, 3, 4, 5], dtype=np.int16)

# array = array.astype(np.int16) # convert to a specific data type.

print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")

#------------------------------------------------------------------------------------------------------------------------------

# ---> Array creation
print(f'\nArray creation')

# 1. np.array() # Creates a NumPy array from an existing Python list, tuple, or other iterable.

arr = np.array([1,2,3,4,5,6,7,8,9])
print(f'\n{arr}')

# 2. np.zeros(shape) # Creates an array filled entirely with 0s.

arr1 = np.zeros((2,3))
print(f'\n{arr1}')

# 3. np.ones(shape) # Creates an array filled with 1s.

arr2 = np.ones((3,4))
print(f'\n{arr2}')

# 4. np.full(shape,fill_value) # Creates an array filled with any value you specify.

arr3 = np.full((4,5),7)
print(f'\n{arr3}')

# 5. np.eye(rows,colns) # Creates an identity-like matrix with 1s on the main diagonal and 0s elsewhere. It can be non square also.

arr4 = np.eye(3)
print(f'\n{arr4}')

# 6. np.identity(size) # Creates a square identity matrix. Unlike np.eye(), It must be square.

arr5 = np.identity(5)
print(f'\n{arr5}')

# 7. np.arange(start,stop,step) # Creates evenly spaced numbers using a start, stop, and step value. # Works similarly to Python's range(), but returns a NumPy array.

arr6 = np.arange(1,50,2)
print(f'\n{arr6}')

# 8. np.linspace(start,stop,num) # Creates evenly spaced numbers between a start and stop value by specifying the number of values you want. Unlike arange(), it does not use a step size.

arr7 = np.linspace(1,50,10)
print(f'\n{arr7}')

#------------------------------------------------------------------------------------------------------------------------------

# ---> Array dimensions - 
print(f'\nArray dimensions')

'''

0D → A single value (point)
1D → A line (list)
2D → A table (rows and columns)
3D → A stack of tables
nD → Multiple stacked dimensions (used for tensors)

You can find the number of dimensions of any NumPy array using : array.ndim

'''

# 1. 0D - no rows or columns and it is also called as scalar.

arr8 = np.array(7)
print(f'\n{arr8}')
print('Dimens : ',arr8.ndim)

# 2. 1D - A 1D array is simply a list of values. It has only one axis.

arr9 = np.array([10,20,30,40,50])
print(f'\n{arr9}')
print('Dimens : ',arr9.ndim)

# 3. 2D - A 2D array has rows and columns. It looks like a spreadsheet or table.

arr10 = np.array([
    [10,20,30,40,50],
    [60,70,80,90,100]
])
print(f'\n{arr10}')
print('Dimens : ',arr10.ndim)

# 4. 3D - A 3D array is a collection (stack) of 2D arrays. Think of it as multiple tables stacked on top of each other.
# Consists of depth/layers, rows, columns

arr11 = np.array([
    [
        [10,20],
        [30,40]
    ],
    [
        [50,60],
        [70,80]
    ]
])
print(f'\n{arr11}')
print('Dimens : ',arr11.ndim)

# 5. nD - An nD array means an array with any number of dimensions greater than or equal to 1.

''''
Why are Dimensions Important in AI?
---> AI models rarely work with single numbers. They process large collections of data, which naturally have multiple dimensions.

Tensor - A tensor is simply a generalized term for a multi-dimensional array.

0D - Scalar - One temperature reading
1D - Vector - List of student marks
2D - Matrix - Spreadsheet or grayscale image
3D - Tensor - RGB image (Height × Width × Channels)
nD - Tensor - 	Batches of images, videos, and other AI data

'''

arr12 = np.array([
    [
        [10,20,0],
        [30,40,0]
    ],
    [
        [50,60,0],
        [70,80,0]
    ]
])
print(f'\n{arr12}')
print('Shape : ',arr12.shape)

