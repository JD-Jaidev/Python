import numpy as np

#------------------------------------------------------------------------------------------------------------------------------

# Arithmetic operators
print(f'\nArithmetic operators ------------------------------------------------------------------------------------------------------------------------------')

# Arithmetic operators in NumPy perform element-wise operations on arrays. This means the operation is applied to each corresponding element of the arrays.
# Note: For operations between two arrays, both arrays should have the same shape (or be compatible through broadcasting).


a = np.array([10, 20, 30])
b = np.array([2, 5, 3])

# Addition  
print(f'\nAddition : {a + b}')

# Subtraction  
print(f'\nSubtraction : {a - b}')

# Multiplication  
print(f'\nMultiplication : {a * b}')

# Division  
print(f'\nDivision : {a / b}')

# Floor division  
print(f'\nFloor division : {a // b}')

# Exponent  
print(f'\nExponent : {a ** b}')

# Modulus  
print(f'\nModulus : {a % b}')

#------------------------------------------------------------------------------------------------------------------------------

# Universal functions
print(f'\nUniversal functions ------------------------------------------------------------------------------------------------------------------------------')

'''

Universal Functions (ufuncs) are built-in NumPy functions that perform fast element-wise operations on arrays.
They work similarly to arithmetic operators (+, -, *, etc.), but are functions instead of operators.

Why use ufuncs?

Faster than Python loops
Works element-wise on arrays
Supports broadcasting
Easier to use in complex calculations

'''

a = np.array([10, 20, 30])
b = np.array([2, 5, 3])

# Addition  
print(f'\nAddition : {np.add(a,b)}')

# Subtraction  
print(f'\nSubtraction : {np.subtract(a,b)}')

# Multiplication  
print(f'\nMultiplication : {np.multiply(a,b)}')

# Division  
print(f'\nDivision : {np.divide(a,b)}')

# Exponent  
print(f'\nExponent : {np.power(a,b)}')

#------------------------------------------------------------------------------------------------------------------------------

# Mathematical functions
print(f'\nMathematical functions ------------------------------------------------------------------------------------------------------------------------------')

# 1. np.sqrt() - Returns the square root of each element.

a = np.array([4, 9, 16, 25])
print(f'\nSqrt : {np.sqrt(a)}')

# 2. np.square(array) - Squares each element.

a = np.array([2, 3, 4])
print(f'\nSquare : {np.square(a)}')

# 3. np.abs(array) - Returns the absolute value (removes the negative sign).

a = np.array([-5, -2, 3, -8])
print(f'\nAbs : {np.abs(a)}')

# 4. np.clip(array, min, max) - Limits values to a specified minimum and maximum.

a = np.array([5, 15, 25, 35])
print(f'\nClip : {np.clip(a, 10, 30)}')

# 5. np.maximum(a, b) - Returns the larger value from two arrays element by element. Checks colmn wise

a = np.array([10, 50, 30])
b = np.array([20, 40, 35])
print(f'\nMaximum : {np.maximum(a, b)}')

# 6.  np.minimum(a, b) - Returns the smaller value from two arrays element by element. Checks colmn wise

a = np.array([10, 50, 30])
b = np.array([20, 40, 35])
print(f'\nMinimum : {np.minimum(a, b)}')

#------------------------------------------------------------------------------------------------------------------------------

# Exponential & Logarithmic functions
print(f'\nExponential & Logarithmic functions ------------------------------------------------------------------------------------------------------------------------------')

# Exponential and logarithmic functions in NumPy perform mathematical operations element-wise on every array element.
# These functions are used extensively in AI, Machine Learning, Deep Learning, and Data Science, especially in activation functions, probability, and loss functions.

# 1. 