import numpy as np

#------------------------------------------------------------------------------------------------------------------------------
# PERFORMANCE  
print(f'\nPerformance')

'''
Performance refers to how fast and memory-efficient your code runs.

NumPy is much faster than normal Python because it :

- Uses optimized C code internally.
- Stores data in contiguous memory.
- Supports vectorized operations instead of Python loops.
- Avoids unnecessary copying of data.

For AI, Machine Learning, and Data Science, writing efficient NumPy code is important because datasets can contain millions of values.

1. Vectorization - 
What is Vectorization?
Vectorization means performing an operation on an entire array at once, instead of processing one element at a time with a loop.
NumPy uses highly optimized C code internally, making vectorized operations much faster than Python loops.


2. Why Python Loops Are Slow - 
Python loops execute one element at a time.
Every iteration requires Python to :
Read the next value.
Execute loop logic.
Perform multiplication.
Move to the next iteration.
This overhead becomes very expensive for large arrays.

3. Views vs Copies - 
View -
A view shares the same memory as the original array.
Changing the view also changes the original array.
Copy - 
A copy creates completely new memory.
Changing the copy does not affect the original array.

Differences - 
View	                    -  Copy
Shares memory	            -  Creates new memory
Faster	                    -  Slightly slower
Less memory	                -  More memory
Changes affect original	    - Changes do not affect original

4. Memory Usage - 
Large datasets consume a lot of memory.
You can check how much memory an array uses.
We can check the amount of memory used by using the array.nbytes(). Also then check the datatype & also reduce memory usage by changing datatype to int32 or lower.

| Data Type | Bytes per Element |
| --------- | ----------------: |
| int8    |                 1 |
| int16   |                 2 |
| int32   |                 4 |
| int64   |                 8 |
| float32 |                 4 |
| float64 |                 8 |

5. Efficient Slicing - 
Slicing usually returns a view, not a copy.

6. Data Types (dtype = np.<datatype>) - 
Choosing the correct data type improves performance and reduces memory usage.
For AI, float32 is commonly used because it uses less memory than float64 while providing sufficient precision.

7. In-place Operations -
Instead of creating a new array, you can just modify the existing array.

8. Broadcasting -
Broadcasting avoids writing loops by automatically expanding compatible arrays.

'''

# 1. Eg for vectorization - 
numbers = [1, 2, 3, 4, 5]
result = []
for i in numbers:
    result.append(i * 2)
print(f'\nWithout vectorization : {result}')


numbers = np.array([1, 2, 3, 4, 5])
result = numbers * 2
print(f'\nWith vectorization : {result}')

# 3. Eg for views vs. copies - also changes the original array 
a = np.array([1,2,3,4])
b = a.view()
b[0] = 100
print(f'\nOriginal array (view) : {a}')
print(f'After array (view) : {b}')

a = np.array([1,2,3,4])
b = a.copy()
b[0] = 100
print(f'\nOriginal array (copy) : {a}')
print(f'After array (copy) : {b}')

# 4. Eg for Memory usage - 
a = np.array([1,2,3,4])
print(f'\nOriginal bytes : {a.nbytes}')
print(f'\nOriginal type : {a.dtype}')

a = np.array([1,2,3,4],dtype = np.int16)
print(f'\nChanged bytes : {a.nbytes}')
print(f'\nChanged type : {a.dtype}')

# 5. Eg for Efficient slicing -
a = np.array([10,20,30,40,50])
b = a[1:4]
print(f'\nEfficient Slicing : {b}')

# 7. Eg for In place operations -
a = np.array([1,2,3])
# a = a + 5  instead of using this
a += 5 # instead use this
print(f'\nSame array : {a}') # This avoids allocating a new array and is generally more memory-efficient.

# 8. Eg for Broadcasting -
a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([10,20,30]) # it considers as - [[10,20,30],[10,20,30]]
print(f'\nBroadcasted : {a + b}')
print(f'\nBroadcasted : {a * b}')
# Instead of using nested loops, NumPy broadcasts b across each row and performs the operation efficiently.

'''

Best Practices for Fast NumPy Code -
- Use vectorized operations instead of Python loops.
- Take advantage of broadcasting rather than manually repeating values.
- Use slicing instead of copying data when you don't need a separate array.
- Use .copy() only when you need an independent array.
- Choose an appropriate dtype (float32, int32, etc.) to reduce memory usage.
- Prefer in-place operations (+=, *=, etc.) when appropriate.
- Avoid repeatedly creating unnecessary temporary arrays.

'''