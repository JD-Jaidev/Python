import numpy as np

#------------------------------------------------------------------------------------------------------------------------------
# MATHEMATICAL OPERATORS

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

# 1. np.exp(array) - Returns e raised to the power of each element. Here, e ≈ 2.71828 (Euler's number).

a = np.array([1, 2, 3])
print(f'\nExp : {np.exp(a)}')

'''

Explanation:
e¹ = 2.718
e² = 7.389
e³ = 20.086

Use in AI: 
Softmax activation
Sigmoid activation
Probability calculations

'''

# 2. np.log(array) - Returns the natural logarithm (base e) of each element. It is the inverse of np.exp().

b = np.array([1, np.e, np.e**2])
print(f'\nLog : {np.log(b)}')

'''

Explanation:
ln(1) = 0
ln(e) = 1
ln(e²) = 2

Use in AI: 
Cross-Entropy Loss
Log Loss
Probability computations

Note: Logarithms are only defined for positive numbers. Using 0 or negative values results in -inf or nan.

'''

# 3. np.log2(array) - Returns the logarithm with base 2.

b = np.array([1, 2, 4, 8, 16])
print(f'\nLog2 : {np.log2(b)}')

'''

Explanation:
log₂(1) = 0
log₂(2) = 1
log₂(4) = 2
log₂(8) = 3
log₂(16) = 4

Use in AI:
Information theory
Entropy calculations
Binary-related computations

'''

# 4. np.log10(array) - Returns the logarithm with base 10.

b = np.array([1, 10, 100, 1000])
print(f'\nLog10 : {np.log10(b)}')

'''

Explanation:
log₁₀(1) = 0
log₁₀(10) = 1
log₁₀(100) = 2
log₁₀(1000) = 3

Use in AI:
Scientific calculations
Data visualization
Signal processing

'''

# np.exp() and np.log() are inverse operations.

#------------------------------------------------------------------------------------------------------------------------------

# Trigonometric functions
print(f'\nTrigonometric functions ------------------------------------------------------------------------------------------------------------------------------')

# Trigonometric functions in NumPy perform element-wise trigonometric calculations on arrays.
# Important: NumPy expects angles in radians, not degrees. To convert degrees to radians, use : np.radians(degrees)

# 1. np.sin(array) - Returns the sine of each angle.

angles = np.array([0, 30, 45, 60, 90])
radians = np.radians(angles)

print(f'\nSin() : {np.sin(radians)}')

'''
Use in AI :
Signal processing
Robotics
Computer graphics
''' 

# 2. np.cos(array) - Returns the cosine of each angle.

angles = np.array([0, 30, 45, 60, 90])
radians = np.radians(angles)
print(f'\nCos() : {np.cos(radians)}')

'''
Use in AI : 
Image processing
Robotics
Computer vision
'''

# 2. np.tan(array) - Returns the tangent of each angle.

angles = np.array([0, 30, 45, 60])
radians = np.radians(angles)
print(f'\nTan() : {np.tan(radians)}')

#------------------------------------------------------------------------------------------------------------------------------