import numpy as np

#------------------------------------------------------------------------------------------------------------------------------
# DATA MANIPULATION  
print(f'\nData manipulation')

# Data manipulation refers to modifying, rearranging, repeating, limiting, or extracting elements from NumPy arrays.
# These functions help you prepare and transform data before using it for data analysis, machine learning, or scientific computing.

# 1. np.unique(array) - Returns the unique (distinct) values from an array in sorted order.
arr = np.array([1, 2, 2, 3, 1, 4, 4, 5])
print(f'\nOriginal array : {arr}')
print(f'\nUnique elements : {np.unique(arr)}')

# 2. np.clip(array,min,max) - Limits all values to a specified minimum and maximum.
arr = np.array([5, 10, 15, 20, 25])
print(f'\nOriginal array : {arr}')
print(f'\nClipped array : {np.clip(arr, 10, 17)}')
# Values less than 10 become 10.
# Values greater than 20 become 20.

# 3. np.repeat(array,<times>) - Repeats each element a specified number of times.
arr = np.array([1, 2, 3])
print(f'\nRepeated array : {np.repeat(arr, 5)}')

# 4. np.tile(array,<times>) - Repeats the entire array multiple times.
arr = np.array([1, 2, 3])


arr = np.array([[1, 2],
                [3, 4]])
print(f'\nRepeated array : {np.tile(arr, 3)}')

'''
Difference Between repeat() and tile()

Function	-  Repeats
repeat()	-  Individual elements
tile()	    -  Entire array
'''

# 5. np.take(array,<indices>) - Selects elements using their indices.
arr = np.array([10, 20, 30, 40, 50])
print(f'\nTaken array : {np.take(arr, [0, 2, 4])}')

# 6. np.put(array,<indices>,<elmnts>) - Replaces elements at specified indices. Original array is modified.
arr = np.array([10, 20, 30, 40, 50])
np.put(arr, [1, 3], [200, 400])
print(f'\nReplaced array : {arr}')

# 7. np.flip(arr) - Reverses the order of elements.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(f'\nFlipped array : {np.flip(arr)}')

arr = np.array([[1, 2],
                [3, 4]])
print(f'\nRow flipped : {np.flip(arr, axis = 0)}')

arr = np.array([[1, 2],
                [3, 4]])
print(f'\nColumn flipped : {np.flip(arr, axis = 1)}')

# 8. np.roll(array,<no>) - Circularly shifts elements. Elements that move past one end reappear at the other end.
arr = np.array([1, 2, 3, 4, 5])
print(f'Rolled 2 : {np.roll(arr, 2)}') # It always works from right to left. So if i give 2 it shifts the rightmost 2 elmnts to the leftmost.
print(f'Rolled 4 : {np.roll(arr, 4)}')