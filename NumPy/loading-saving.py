import numpy as np

print('\nLoading & Saving data in NumPy')

'''
Loading and saving data means storing NumPy arrays in files so you can use them later without recreating them.

NumPy provides functions to save arrays in :
Binary format (.npy) → Faster and preserves data types.
Text format (.txt, .csv) → Human-readable and easy to share.
'''

# 1. np.save(filename, array)

'''
Saves a NumPy array in binary (.npy) format.
Fast to read and write.
Preserves the array's shape and data type (dtype).
Best choice when working only with NumPy.
'''

arr = np.array([10, 20, 30, 40])
np.save("numbers.npy", arr)

# 2. np.load(filename) - Loads a previously saved .npy file.

arr = np.load("numbers.npy")
print(f'\nPrint loaded array : {arr}')

# 3. np.savetxt(filename, array)

'''
Saves an array as a text file.
Useful when you want :
A human-readable file.
To open it in Excel or a text editor.
To share data with other programs.
'''

arr = np.array([[1, 2],
                [3, 4]])
np.savetxt("data.txt", arr)
print('Saved as txt file')

np.savetxt("data.csv", arr, delimiter = ",")
print('Saved as csv file : ')

# The delimiter = "," separates values with commas, creating a CSV (Comma-Separated Values) file.

# 4. np.loadtxt(filename) - Loads data from a text or CSV file.

arr = np.loadtxt("data.txt")
print(f'\nLoaded text file : {arr}')

arr = np.loadtxt("data.csv" , delimiter = ',')
print(f'\nLoaded csv file : {arr}')

'''

.npy vs .txt
Feature	                -  .npy	    -  .txt / .csv
Speed	                -  Fast	    -  Slower
Human-readable	        -  No	    -  Yes
Preserves shape	        -  Yes	    -  Yes
Preserves data type	    -  Yes	    -  Usually loaded as float64 unless specified
Best for NumPy	        -  Yes	    -  No
Easy to share	        -  Less	    -  Yes

'''