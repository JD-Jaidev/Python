import numpy as np

#------------------------------------------------------------------------------------------------------------------------------
# LINEAR ALGEBRA 
print(f'\nLinear algebra')

# Linear Algebra is the branch of mathematics that deals with vectors, matrices, and matrix operations.
# In AI, Machine Learning, Computer Vision, and Deep Learning, almost everything is represented as matrices (datasets, images, neural network weights, embeddings, etc.).

#------------------------------------------------------------------------------------------------------------------------------ 
# 1. Matrix multiplication
print(f'\nMatrix multiplication ------------------------------------------------------------------------------------------------------------------------------')

# 1. np.dot() -
'''
Performs the dot product.
1D arrays → Dot product of vectors.
2D arrays → Matrix multiplication.
Higher dimensions → More advanced behavior.
'''

a = np.array([1,2,3])
b = np.array([4,5,6])
print(f'\nDot product : {np.dot(a,b)}')

# Eg - matrices
a = np.array([[1,2],
              [3,4]])
b = np.array([[5,6],
              [7,8]])
print(f'\nMatrix dot product : {np.dot(a,b)}') # it performs like normal matrix multplication

# 2. np.matmul(array1,array1) - Specifically performs matrix multiplication.

a = np.array([[1,2],
              [3,4]])
b = np.array([[5,6],
              [7,8]])
print(f'\nMatmull : {np.matmul(a,b)}')

# 3. @ operator print(array1 @ array2) - @ is simply a shorter way to write matmul().

a = np.array([[1,2],
              [3,4]])
b = np.array([[5,6],
              [7,8]])
print(f'\n@ Operator : {a @ b}')

#------------------------------------------------------------------------------------------------------------------------------ 
# 2. Matrix transformation
print(f'\nMatrix transformation ------------------------------------------------------------------------------------------------------------------------------')

# np.transpose (.T) - Swaps rows and columns. or print(np.transpose(a))
a = np.array([[1,2,3],
              [4,5,6]])
print(f'\nTranspose : {a.T}')

#------------------------------------------------------------------------------------------------------------------------------ 
# 3. Vector operations
print(f'\nVector operations ------------------------------------------------------------------------------------------------------------------------------')

# 1. np.inner(array1 , array2) -  Computes the inner product (similar to dot product for 1D arrays).

a = np.array([1,2,3])
b = np.array([4,5,6])
print(f'\nInner : {np.inner(a,b)}')

# 2. np.outer(array1 , array2) - Computes the outer product. Each element of one vector is multiplied by every element of the other vector.

a = np.array([1,2,3])
b = np.array([4,5])
print(f'\nOuter : {np.outer(a,b)}')

'''
1 × [4,5]
2 × [4,5]
3 × [4,5]
'''

# 3. np.cross(array1 , array2) - Computes the cross product of 3D vectors.

a = np.array([1,0,0])
b = np.array([0,1,0])
print(f'\nCross : {np.cross(a,b)}')

'''
if a = [a₁, a₂, a₃] & b = [b₁, b₂, b₃]

then a × b =
[
 a₂b₃ - a₃b₂,
 a₃b₁ - a₁b₃,
 a₁b₂ - a₂b₁
]
'''

'''
Common in -
Physics
Robotics
Computer Graphics
'''

#------------------------------------------------------------------------------------------------------------------------------ 
# 4. numpy.linalg
print(f'\nnumpy.linalg ------------------------------------------------------------------------------------------------------------------------------')
# Contains advanced linear algebra functions.

import numpy.linalg as la