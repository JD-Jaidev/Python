import numpy as np

#------------------------------------------------------------------------------------------------------------------------------
# STATISTICAL OPERATORS
print(f'\Statistical operators ------------------------------------------------------------------------------------------------------------------------------')

# 1. np.sum(array) - Returns sum of all elements.

a = np.array([10, 20, 30, 40, 50])
print(f'\nSum : {np.sum(a)}')

# 2. np.mean(array) - Returns the average (mean) of all elements.

print(f'\nMean : {np.mean(a)}')

'''
Use in AI: 
Data normalization
Feature scaling
Statistics
'''

# 3. np.median(array) - Returns the middle value after sorting.

a = np.array([10, 30, 20, 50, 40]) # [10,20,30,40,50]

print(f'\nMedian : {np.median(a)}')

'''
Use in AI:
Handling outliers
Data preprocessing
'''

# 4. np.std(array) - Returns the standard deviation, which measures how spread out the values are from the mean.

print(f'\nStandard deviation : {np.std(a)}')

'''
Use in AI:
Data normalization
Feature scaling
Statistics
'''

# 5. np.var(array) - Returns the variance, which measures the spread of data. It is the square of the standard deviation.

print(f'\nVariance : {np.var(a)}')

'''
Use in AI: 
Statistics
Feature analysis
'''

# 6. np.min(array) - Returns the smallest value.

print(f'\nMinimum : {np.min(a)}')

'''
Use in AI: 
Data normalization
Finding minimum values
'''

# 7. np.max(array) - Returns the largest value.

print(f'\nMaximum : {np.max(a)}')

'''
Use in AI
Feature scaling
Finding maximum values
'''

# 8. np.argmin(array) - Returns the index of the smallest value, not the value itself.

print(f'\nArgmin : {np.argmin(a)}')

'''
Use in AI:
Finding positions of minimum values
'''

# 9. np.argmax(array) - Returns the index of the largest value, not the value itself.

print(f'\nArgmax : {np.argmax(a)}')

'''
Use in AI:
Finding the predicted class in classification models
Selecting the highest probability
'''

# 10. np.percentile(array, percentile) - Returns the value below which a given percentage of the data falls.
# It gives the values from the sorted array

print(f'\nPercentile : {np.percentile(a, 25)}')
print(f'\nPercentile : {np.percentile(a, 75)}')

'''
Use in AI: 
Detecting outliers
Data analysis
'''