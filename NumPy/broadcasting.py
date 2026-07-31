import numpy as np

#------------------------------------------------------------------------------------------------------------------------------
# BROADCASTING 
print(f'\nBroadcasting ------------------------------------------------------------------------------------------------------------------------------')

# Broadcasting is a feature in NumPy that allows arrays of different shapes to perform arithmetic operations without manually resizing them.
# Instead of copying data, NumPy virtually expands the smaller array's dimen to match the larger array, making operations much faster and memory-efficient.

# The dimensions have the same size or one of the dimensions has a size of one.

'''
For eg - 
if array1 = 4 x 3 and array2 = 1 x 3
so [5 , 5] here the rows of both arrays match
   [5 , 1] here the colums of both arrays has a either 1
so the rows or colmns in both of them must be either same or either one dimen is 1 
'''

'''
Broadcasting rules : 

Rule 1: Compare shapes from the right - NumPy always starts comparing dimensions from the last (rightmost) dimension.
Rule 2: Dimensions are compatible if - They are equal. or One of them is 1.
Rule 3: Missing dimensions are treated as 1
'''

array1 = np.array([
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
])

array2 = np.array([
    [60],
    [70],
    [80],
    [90],
    [100]
])

print(array1.shape)
print(array2.shape)

print(array1 * array2)

#------------------------------------------------------------------------------------------------------------------------------

# 1D + 2D broadcasting

array1 = np.array([10,20,30,40,50]) # first add this with 1st row and then 2nd row of array2
array2 = np.array()

print(array1.shape)
print(array2.shape)

print(array1 * array2)

# Visualising this - 
'''
array1 will become = [[10,20,30,40,50]
                      [10,20,30,40,50]]
array2 will be = [[1,2,3,4,5],
                  [6,7,8,9,10]]
'''
#------------------------------------------------------------------------------------------------------------------------------

print(f'\Vectorized operations ------------------------------------------------------------------------------------------------------------------------------')

# A vectorized operation means performing an operation on an entire NumPy array at once, instead of using loops.
# NumPy executes these operations using optimized C code internally, making them much faster than Python for loops.
