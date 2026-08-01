import numpy as np

#------------------------------------------------------------------------------------------------------------------------------
# RANDOM DISTRIBUTIONS   
print(f'\nRandom distributions')
# A random distribution is a way of generating random numbers that follow a specific pattern instead of being completely arbitrary.

# 1. np.random.normal(loc, scale, size)

'''
loc → Mean (center of the distribution)
scale → Standard deviation (spread)
size → Number or shape of values to generate

Generates random numbers that follow a Normal (Gaussian) distribution.
A normal distribution is the famous bell-shaped curve, where:
Most values are near the mean.
Fewer values appear as you move farther from the mean.

Common Uses -
Machine Learning
Deep Learning (weight initialization)
Human heights
Exam scores
Measurement errors
'''

arr = np.random.normal(loc = 50, scale = 5, size = 10)
print(f'\nNormal : {arr}')

# 2. np.random.uniform(low, high, size)
# Generates random numbers where every value within a range has an equal chance of occurring.
# Unlike the normal distribution, there is no center bias.

arr = np.random.uniform(10, 20, 5)
print(f'\nUniform : {arr}')

'''
Common Uses -
Random sampling
Simulations
Random positions in games
Data augmentation
'''

# 3. np.random.binomial(n, p, size)

'''
Generates random numbers from a Binomial Distribution.
A binomial distribution models the number of successes in a fixed number of independent trials.
Each trial has only two possible outcomes :
Success
Failure

Parameters -
n → Number of trials
p → Probability of success
size → Number or shape of samples (no. of trials)

Eg - tossing fair coin 10 times
Trial 1 → 6 heads
Trial 2 → 5 heads
Trial 3 → 4 heads
'''

arr = np.random.binomial(n = 10, p = 0.5, size = 5)
print(f'\nBinomial : {arr}')

# 4. np.random.poisson(lam, size)
# Generates random numbers following a Poisson Distribution.
# A Poisson distribution models the number of times an event happens within a fixed interval (time, distance, area, etc.).

'''
lam → Average number of events (λ)
size → Number or shape of samples

On an avg if there are 3 calls per calls.
Minute 1 → 2 calls
Minute 2 → 3 calls
Minute 3 → 5 calls
Minute 4 → 1 call
'''

arr = np.random.poisson(lam = 3, size = 10)
print(f'\nPoisson : {arr}')