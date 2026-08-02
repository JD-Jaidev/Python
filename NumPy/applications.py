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
4. Matrix Multiplication - 
Almost every neural network layer performs matrix multiplication.

AI Use -
input x weights

5. Dot Products -
Measures how similar two vectors are.

AI Use -
Neural Networks
Similarity calculations
Embeddings

6. Distance Calculations -
Measures how far apart two points are.

AI Use -
KNN
Clustering
Recommendation Systems

7. Cosine Similarity - cos = (A·B) / (||A|| ||B||))
Measures the angle between vectors instead of distance.

AI Use - 
Chatbots
Search Engines
Sentence Embeddings
Recommendation Systems

8. Images as Arrays -
Computers store images as NumPy arrays.

AI Use - 
OpenCV
Image Classification
Object Detection

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

# 4. Matrix multiplication -
A = np.array([[1,2],
              [3,4]])
B = np.array([[5,6],
              [7,8]])
print(f'\nMatrix multiplication : {A @ B}')

# 5. Dot product - 
a = np.array([1,2,3])
b = np.array([4,5,6])
print(f'\nDot product : {np.dot(a,b)}')

# 6. Distance calculations - 
a = np.array([1,2])
b = np.array([4,6])
distance = np.linalg.norm(a - b) # norm - magnitude
print(f'\nDistance calculations : {distance}')

# 7. Cosine similarity - 
A = np.array([1,2])
B = np.array([2,4])
similarity = np.dot(A,B) / (np.linalg.norm(A) * np.linalg.norm(B))
print(f'\nCosine similarity : {similarity}')

# 8. Images as arrays -
image = np.array([
    [0,255],
    [128,64]
])
print(f'\nImages as arrays : {image}')
# Each number represents a pixel intensity.