# PANDAS

'''

1. Introduction -
Pandas is one of the most important Python libraries for data analysis, data manipulation, and data cleaning. 
It provides easy-to-use data structures for working with structured data such as CSV files, Excel files, SQL databases, and JSON data.

Pandas is a Python library that helps you store, organize, filter, analyze, and manipulate data in a table-like format.
Think of it like an Excel spreadsheet inside Python.

2. Why use Pandas?

Without Pandas, handling large datasets using lists and dictionaries becomes difficult.
Pandas makes it easy to -
Read CSV and Excel files
Clean missing values
Filter data
Sort data
Analyze statistics
Merge datasets
Prepare data for Machine Learning

3. Series -
A Series is a one-dimensional labeled array.
It is similar to a single column in Excel.
It can store -
integers
floats
strings
booleans
objects

4. DataFrame -
A DataFrame is a two-dimensional table made up of rows and columns.
Think of it as an Excel spreadsheet.

5. Index -
The Index uniquely identifies each row.
By default, Pandas starts indexing from 0.

6. Columns -
Columns represent different features or variables.

7. Rows -
Rows represent individual records.

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Creating Data in Pandas - 
Pandas allows you to create or load data from various sources such as lists, dictionaries, NumPy arrays, CSV files, Excel files, and JSON files. 
The two main data structures are Series (1D) and DataFrame (2D).

1. Creating Data from Lists -
A Python list can be converted into a Series or a DataFrame.

2. Creating Data from Dictionaries -
A dictionary is one of the most common ways to create a DataFrame. Each key becomes a column, and each value (list) becomes the column data.

3. Creating Data from NumPy Arrays -
Since Pandas is built on NumPy, you can directly convert NumPy arrays into a DataFrame.

4. Creating Data from CSV Files -
A CSV (Comma-Separated Values) file stores data in plain text, with values separated by commas. It is the most common format for datasets in AI and Data Science.

5. Creating Data from Excel Files -
Excel files (.xlsx) can also be loaded into Pandas.

6. Creating Data from JSON Files -
JSON (JavaScript Object Notation) stores data in a key-value format and is commonly used by APIs.



'''

# Eg1 -
import pandas as pd
data = {
    "Name": ["John", "Alice"],
    "Age": [21, 22],
    "City": ["Chennai", "Mumbai"]
}
df = pd.DataFrame(data)
print(f'\n{df}')

# Eg2 -
df = pd.DataFrame({
    "Name": ["John", "Alice", "Bob"],
    "Marks": [85, 92, 78]
})
print(f'\n Original data frame : \n {df}')
print(f'\n{df[df["Marks"] > 80]}')

# Eg3 -
ages = pd.Series([10,20,30,40,50])
print(f'\n{ages}')

ages = pd.Series([10,20,30,40,50], index = ['A','B','C','D','E'])
print(f'\n{ages}')
print(ages["A"]) # accesing the values using index (as we do it by accessing the value using a key in dict)

# Eg4 -
students = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(students)
print(df)
# A DataFrame is simply multiple Series combined together.

# Eg5 -
df = pd.DataFrame({
    "Name": ["John", "Alice", "Bob"]
})
print(f'\n{df.index}') # tells about the current indices values 

# Eg6 -
data = {
    "Name": ["John", "Alice"],
    "Age": [21, 22],
    "City": ["Chennai", "Mumbai"]
}
df = pd.DataFrame(data)
print(f'\n{df.columns}') # coln properties

# Eg7 -
data = {
    "Name": ["John", "Alice"],
    "Age": [21, 22],
    "City": ["Chennai", "Mumbai"]
}
df = pd.DataFrame(data)
print(f'\n{df.loc[1]}') # accessing rows

'''

             Columns
--------------------------------
Index   Name     Age     City
--------------------------------
0       John      21   Chennai
1       Alice     22   Mumbai
--------------------------------
          ↑
         Rows

'''

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Eg1 - Creating data from lists - 
marks = [85, 90, 78, 92]
series = pd.Series(marks)
print(f'Data from lists : \n {series}')

# Creating data from lists as data frame -
students = [
    ['A',10],
    ['B',20],
    ['C',30]
]
df = pd.DataFrame(students,columns = ['Name','Marks'])
print(f'Data as data frame : \n {df}')

# Eg2 - creating data from dict
data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print(f'\n {df}')

# Eg3 -
import numpy as np
arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
df = pd.DataFrame(arr, columns=["A", "B"])
print(f'\n {df}')

# pd.read_csv(<file name>)
# pd.read_excel(<file name>)
# pd.read_json(<file name>)






















