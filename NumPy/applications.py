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
----------------------------------------------------------------------------------------------------------------------------------------------
5. Dot Products -
Measures how similar two vectors are.

AI Use -
Neural Networks
Similarity calculations
Embeddings
----------------------------------------------------------------------------------------------------------------------------------------------
6. Distance Calculations -
Measures how far apart two points are.

AI Use -
KNN
Clustering
Recommendation Systems
----------------------------------------------------------------------------------------------------------------------------------------------
7. Cosine Similarity - cos = (A·B) / (||A|| ||B||))
Measures the angle between vectors instead of distance.

AI Use - 
Chatbots
Search Engines
Sentence Embeddings
Recommendation Systems
----------------------------------------------------------------------------------------------------------------------------------------------
8. Images as Arrays -
Computers store images as NumPy arrays.

AI Use - 
OpenCV
Image Classification
Object Detection
----------------------------------------------------------------------------------------------------------------------------------------------
9. Neural Network Forward Propagation -
A neural network computes. Formula = Output = Input × Weights + Bias

AI Use -
Every neural network layer.
----------------------------------------------------------------------------------------------------------------------------------------------
10. Weight Matrices -
Weights store what the model learns.
Each value is learned during training.
----------------------------------------------------------------------------------------------------------------------------------------------
11. Bias Vectors -
Bias shifts the output.
----------------------------------------------------------------------------------------------------------------------------------------------
12. Tensor Operations -
A tensor is simply a higher-dimensional array.

Scalar → 0D
---> 5
Vector → 1D
---> [1 2 3]
Matrix → 2D
---> [[1 2]
      [3 4]]
Tensor → 3D+

AI Use- 
Deep Learning
CNNs
Transformers
----------------------------------------------------------------------------------------------------------------------------------------------
13. Batch Processing -
Instead of processing one sample at a time, AI processes many samples together.

AI Use -
Training neural networks much faster.
----------------------------------------------------------------------------------------------------------------------------------------------
14. Broadcasting -
Performs operations on arrays of different shapes automatically.
----------------------------------------------------------------------------------------------------------------------------------------------
15. Activation functions -
Used in neural networks

What does the Sigmoid function do?
The sigmoid function converts any real number into a value between 0 and 1.
Large negative numbers → close to 0
Zero → 0.5
Large positive numbers → close to 1

---> Activation functions -
An activation function is a mathematical function used in a neural network to decide how much information should be passed to the next layer.
Without activation functions, a neural network would behave like a simple linear model and would not be able to learn complex patterns.
----------------------------------------------------------------------------------------------------------------------------------------------
16. Random Weight Initialization -
AI models start with random weights before training.
----------------------------------------------------------------------------------------------------------------------------------------------
17. Loss Calculation -
Used to measure prediction error (Mean Squared Error).
----------------------------------------------------------------------------------------------------------------------------------------------
18. Data Shuffling -
Prevents the model from learning patterns based on data order.
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

# 9. Neural network -
X = np.array([[1,2]])
W = np.array([[0.5],
              [0.8]])
b = np.array([0.1])
output = X @ W + b # Z = x_n * w_n + B
print(f'\nNeural network : {output}')

# 10. Weight matrices - 
weights = np.array([[0.3,0.8],
                    [0.5,0.1]])
print(f'\nWeight matrices : {weights}')

# 11. Bias vectors -
bias = np.array([0.5,0.2])
print(f'\nBias vectors : {bias}')

# 12. Tensor operations -
tensor = np.random.rand(2,3,4)
print(f'\Tensor : {tensor.shape}')

# 13. Batch processing -
batch = np.array([
    [1,2],
    [3,4],
    [5,6]
])
print(f'\nBatch processing : {batch.shape}') # (3,2) - 3 samples, 2 features

# 14. Broadcasting -
X = np.array([[1,2],
              [3,4]])
print(f'\nBroadcasting : {X + 10}')

# 15. Activation functions -
x = np.array([-1,0,1])
sigmoid = 1 / (1 + np.exp(-x))
print(f'\nActivation function : {sigmoid}')

# 16. Random weight initialization - 
weights = np.random.randn(3,2)
print(f'\nrandom weight initialization : {weights}')

# 17. Loss calculation -
actual = np.array([1,2,3])
pred = np.array([1.2,1.8,2.9])
loss = np.mean((actual - pred)**2)
print(f'\nLoss calculation : {loss}')

# 18. Data shuffling -
