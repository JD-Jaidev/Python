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

# 1. la.inv(array) - Computes the inverse of a square matrix. 
a = np.array([[1,2],
              [3,4]])
print(f'\nInverse : {la.inv(a)}')

# 2. la.det(array) - Computes the determinant of a square matrix.

a = np.array([[1,2],
              [3,4]])
print(f'\nDeterminant : {la.det(a)}')

# 3. la.norm(array) - Computes the length (magnitude) of a vector or matrix.

a = np.array([3,4])
print(f'\nMagnitude : {la.norm(a)}')

'''
√(3²+4²)
= √25
= 5
'''

# 4. la.solve(array1 , array2) - Solves a system of linear equations.

A = np.array([[1,1], # coefficients
              [2,1]])
B = np.array([5,8]) # equal to value
print(f'\Solve : {la.solve(A,B)}')

'''
A → Coefficient matrix (must be a square matrix)
B → Constant values (right-hand side)
Returns → Solution vector (x)

1x + 1y = 5
2x + 1y = 8
'''

# 5. eig(array) - Eigen values and vectors 

'''
numpy.linalg.eig() is used to find the eigenvalues and eigenvectors of a square matrix.
Eigenvalues tell you how much a transformation stretches or shrinks in certain directions, while eigenvectors tell you those special directions.

Eigen values - These represent the amount by which the matrix stretches or compresses along certain directions.
Eigen vectors - These are the special directions that remain unchanged except for scaling.

Normally, multiplying a vector by a matrix changes both its length and direction.

---> For an eigenvector,

A × v = λ × v

where

A = Matrix
v = Eigenvector
λ (lambda) = Eigenvalue

The vector keeps the same direction, but its length changes by the eigenvalue.

'''

A = np.array([[4, 2], [1, 3]]) 
values, vectors = la.eig(A) 
print(f'\nEigen values :{values}') # each elmnt is an eigen value
print(f'\nEigen vectors : {vectors}') # every coln is an eigen vector

# 6. svd(array) - numpy.linalg.svd() performs Singular Value Decomposition (SVD). It decomposes a matrix into three smaller matrices.

'''

U, S, Vt = la.svd(A)

U → Left singular vectors
S → Singular values
Vt → Right singular vectors (transposed)

'''

A = np.array([[1, 2], [3, 4]]) 
U, S, Vt = la.svd(A) 
print('\nLeft singular vectors : ',U) 
print('\nSingular values :',S) 
print('\nRight singular vectors : ',Vt)

'''

U - Contains the left singular vectors. These describe one set of directions in the transformation.
S - Contains the singular values. These tell you how important each direction is. A larger singular value means that direction carries more information.
Vt - Contains the right singular vectors (transposed). These describe another set of directions used in the decomposition.

'''

