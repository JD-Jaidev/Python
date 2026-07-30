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

