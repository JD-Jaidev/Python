import numpy as np

'''

NumPy applications in AI - 
----------------------------------------------------------------------------------------------------------------------------------------------
1. Feature Scaling -  
Feature scaling makes different features have similar ranges so that machine learning algorithms learn faster and more accurately.

AI Use - 
Gradient Descent
Neural Networks
KNN
SVM
----------------------------------------------------------------------------------------------------------------------------------------------
2. Normalization (Min-Max Scaling) - 
Normalization scales values between 0 and 1. Formula = (x - min) / (max - min)

AI Use - 
Used when features have different units.
Example :
Height
Weight
Salary
----------------------------------------------------------------------------------------------------------------------------------------------
3. Standardization (Z-score) - 
Standardization makes data have
Mean = 0
Standard deviation = 1
Formula = (x - mean) / std

AI Use - 
Logistic Regression
PCA
Neural Networks
----------------------------------------------------------------------------------------------------------------------------------------------


'''


# 1. Feature scaling -
age = np.array([20, 40, 60])
scaled = age / 60
print(f'\nFeature scaled : {scaled}')

# 2. Normalization -
x = np.array([10, 20, 30])
normalized = (x - x.min()) / (x.max() - x.min())
print(f'\nNormalization : {normalized}')

# 3. Standardization -
x = np.array([10, 20, 30])
standardized = (x - x.mean()) / x.std()
print(f'\nStandardization{standardized}')