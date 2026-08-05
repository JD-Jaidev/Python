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

























