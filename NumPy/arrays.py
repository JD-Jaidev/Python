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

#------------------------------------------------------------------------------------------------------------------------------

# ---> Array attributes - 
print(f'\nArray attributes')

'''

Array attributes are built-in properties of a NumPy array that provide information about the array itself. They tell you things like:

- What is its shape?
- How many dimensions does it have?
- How many elements are stored?
- What type of data is stored?
- How much memory does it use?
Unlike methods (such as reshape() or sort()), attributes do not use parentheses.

'''
# Eg -

array1 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

array2 = np.array([
    [
        [10,20,30],
        [40,50,60]
    ],
    [
        [70,80,90],
        [100,True,120]
    ]
])

# 1. array.shape - shape tells you the number of rows and columns (or size of each dimension) of the array. It returns a tuple.

print(f'\nShape : {array1.shape}')
print(f'\nShape : {array2.shape}')

# 2. array.ndim - ndim tells you how many dimensions (axes) an array has.

print(f'\nDimen : {array1.ndim}')
print(f'\nDimen : {array2.ndim}')

# 3. arrary.size - size tells you the total number of elements in the array.

print(f'\nSize : {array1.size}')
print(f'\nSize : {array2.size}')

# 4. array.dtype - dtype stands for Data Type.

# It tells you what type of data every element in the array stores.

# Eg -
# int32
# int64
# float32
# float64
# bool
# complex128

print(f'\ndtype : {array1.dtype}')
print(f'\ndtype : {array2.dtype}')

# Different data types use different amounts of memory and affect computation speed.

# 5. array.itemsize - itemsize tells you how many bytes one element occupies.

print(f'\nItemsize : {array1.itemsize}')
print(f'\nItemsize : {array2.itemsize}')

# dtype = int64
# 64 bits = 8 bytes so each integer occupies 8 bytes

# 6. array.nbytes - nbytes tells you the total memory used by the array.

print(f'\nnbytes : {array1.nbytes}')
print(f'\nnbytes : {array2.nbytes}')

# 7. array.T - T stands for Transpose. Coverts rows to columns and vice versa

print(f'\nT : {array1.T}')
print(f'\nT : {array2.T}')

# 8. array.flags - flags provides information about how the array is stored in memory, such as whether it is contiguous and whether it is writable.

print(f'\nFlags : {array1.flags}')
print(f'\nFlags : {array2.flags}')

'''

1. C_CONTIGUOUS : True - This tells you whether the array is stored in C-style (row-major) order.
2. F_CONTIGUOUS : False - This checks whether the array is stored in Fortran-style (column-major) order.
3. OWNDATA : True - This tells you whether the array owns its own memory.
4. WRITEABLE : True - This tells whether the array can be modified.
5. ALIGNED : True - This tells whether the data is stored at proper memory boundaries for your computer's processor.
6. WRITEBACKIFCOPY : False - This is an advanced flag. It tells NumPy whether the array is a temporary copy that must be copied back to another array after modifications.

'''

# 9. array.flat - flat returns an iterator that lets you access every element in the array one by one, regardless of its

for value1 in arr.flat:
    print(f'\nValue1 : {value1}')

for value2 in arr.flat:
    print(f'\nValue2 : {value2}')

#------------------------------------------------------------------------------------------------------------------------------

# ---> Datatypes -
print(f'\nArray datatypes')

'''

A data type (dtype) tells NumPy what kind of data is stored in each element of an array.
Every element in a NumPy array has the same data type. This is one of the reasons NumPy is much faster and more memory-efficient than Python lists.

Why are Data Types Important?

Data types determine:

 -The kind of values the array can store (integers, decimals, booleans, etc.)
- How much memory each element uses
- The speed of computations

For example:

- int32 uses 4 bytes per element.
- int64 uses 8 bytes per element.

If you have millions of numbers, choosing the right data type can save a lot of memory.

'''

# 1. int32 - Stores 32-bit integers (whole numbers).
# Size: 4 bytes
# Range: −2,147,483,648 to 2,147,483,647

dt1 = np.array([10, 20, 30], dtype=np.int32)

print(f'\n{dt1}')
print(f'DATATYPE : {dt1.dtype}')

# 2. int64 - Stores 64-bit integers.
# Size: 8 bytes
# Can store much larger integers than int32

dt2 = np.array([10000000000, 20000000000], dtype = np.int64)

print(f'\n{dt2}')
print(f'DATATYPE : {dt2.dtype}')

# 3. float32 (most importtant in AI) - Stores 32-bit floating-point (decimal) numbers.
# Size: 4 bytes
# Faster and uses less memory than float64

dt3 = np.array([1.5, 2.7, 3.9], dtype = np.float32)

print(f'\n{dt3}')
print(f'DATATYPE : {dt3.dtype}')

# Most deep learning libraries (such as TensorFlow and PyTorch) use float32 by default because it provides a good balance between speed, memory usage, and numerical precision.

# 4. float64 - Stores 64-bit floating-point (decimal) numbers.
# Size: 8 bytes
# More precise than float32
# Uses more memory

dt4 = np.array([1.5, 2.7, 3.9], dtype = np.float64)

print(f'\n{dt4}')
print(f'DATATYPE : {dt4.dtype}')

# 5. bool - Stores Boolean values: True, False

dt5 = np.array([True, False, True])

print(f'\n{dt5}')
print(f'DATATYPE : {dt5.dtype}')


# Changing the Data Type - You can convert an existing array to another data type using astype().

datatype = np.array([1, 2, 3])
new_arr = datatype.astype(np.float32)
print(f'\n{new_arr}')
print(f'New data type : {new_arr.dtype}')

#------------------------------------------------------------------------------------------------------------------------------

# ---> Array indexing - Array indexing is the process of accessing one or more specific elements from a NumPy array using their position (index).
# indexing starts with 0

ind1 = np.array([10,20,30,40,50])

ind2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

ind3 = np.array([
    [
        [10,20,30],
        [40,50,60]
    ],
    [
        [70,80,90],
        [100,110,120]
    ]
])

# 1. Positive indexing  -
print(f'\nPositive Indexing : {ind1[4]}')

# 2. Negative indexing  -
print(f'\nNegative Indexing : {ind1[-2]}')

# 3. 1D array indexing  -
print(f'\n1D array Indexing : {ind1[3]}')

# 4. 2D array indexing  - array[row,colm]
print(f'\n2D array Indexing : {ind2[1,1]}')

# 5. 3D array indexing  - array(layer,row,colm)
print(f'\n3D array Indexing : {ind3[1,0,2]}')

# 6. Boolean indexing - Boolean indexing selects elements based on a condition.
print(f'\nBoolean Indexing : {ind3[ind3 > 50]}') # gives a single list of values

# 7. Fancy (Advanced) Indexing - Fancy indexing lets you access multiple specific elements at once using an array or list of indices.
print(f'\n2D array Fancy Indexing : {ind2[[0,1]]}')
print(f'\n3D array Fancy Indexing : {ind3[[1,0]]}')

#------------------------------------------------------------------------------------------------------------------------------

