# DATA DISPLAY AND CHART WIDGETS
# These widgets are used to display tables, edit data, and visualize information using built-in or third-party charting libraries.

import streamlit as st
import pandas as pd
import time

#-------------------------------------------------------------------------------------------------------------------------
# 1. Dataframes
# Purpose - Scrolling, Sorting, Resizing columns, Searching (browser-supported), Column reordering
#Uses Student records, Sales reports, ML datasets\

# st.dataframe()
st.write('---------------------------- DATAFRAMES')

'''st.dataframe(
    data = '<data to be displayed>',
    width = None,
    height = None,
    use_container_width = False,
    hide_index = False
)'''

'''

Parameter	-  Description
data	-  DataFrame, list, NumPy array, etc.
width	-  Width of the table
height	-  Height of the table
use_container_width	 -  Expand to full container width
hide_index	-  Hide row index

'''

# Eg - 
df = pd.DataFrame({
    "Name": ["Jaidev", "Rahul"],
    "Age": [19, 20]
})
st.dataframe(df)

#-------------------------------------------------------------------------------------------------------------------------

# TABLES 
st.write('---------------------------- TABLES')

# st.table() # Displays a static table. Unlike st.dataframe(), it cannot be sorted or scrolled. Uses - Small reports, Static summaries.

# Eg -
df = pd.DataFrame({
    "Name": ["A", "B"],
    "Marks": [90, 85]
})
st.table(df)

#-------------------------------------------------------------------------------------------------------------------------

# DATA EDITOR
st.write('---------------------------- DATA EDITOR')

# st.data_editor() # Displays an editable table. Users can modify values directly in the browser. Uses - Inventory, Attendance, Budget editing

'''st.data_editor(
    data = '<data to be displayed>',
    num_rows = "fixed",
    use_container_width = False,
    hide_index = False
)'''

# Eg -
df = pd.DataFrame({
    "Name": ["John"],
    "Age": [20]
})
edited = st.data_editor(df)

#-------------------------------------------------------------------------------------------------------------------------

# LINE CHART
st.write('---------------------------- LINE CHART')

# st.line_chart() # Displays a line chart. Uses - Stock prices, Sales trends, Temperature

'''st.line_chart(
    data = '<data to be displayed>',
    x = None,
    y = None,
    color = None
)'''

# Eg -
df = pd.DataFrame({
    "Month": [1,2,3],
    "Sales": [100,150,180]
})
st.line_chart(df, x = "Month", y = "Sales")

#-------------------------------------------------------------------------------------------------------------------------

# BAR CHART
st.write('---------------------------- BAR CHART')

# st.bar_chart() # Displays a bar chart. Uses - Population, Revenue, Product comparison

'''st.bar_chart(
    data = '<data to be displayed>',
    x = None,
    y = None
)'''

# Eg - 
df = pd.DataFrame({
    "City":["Chennai","Delhi"],
    "Population":[10,20]
})
st.bar_chart(df,x = "City",y = "Population")

#-------------------------------------------------------------------------------------------------------------------------

# AREA CHART
st.write('---------------------------- AREA CHART')

# st.area_chart() # Displays an area chart. Uses - Website traffic, growth analysis

# Eg - 
df = pd.DataFrame({
    "Day":[1,2,3],
    "Visitors":[50,70,90]
})
st.area_chart(df,x = "Day",y = "Visitors")

#-------------------------------------------------------------------------------------------------------------------------

# SCATTER PLOT
st.write('---------------------------- SCATTER PLOT')

# st.scatter_chart() # Displays a scatter plot. Uses - ML Dataset, Correlation analysis

'''st.scatter_chart(
    data = '<data to be displayed>',
    x = None,
    y = None
)'''

# Eg -
df = pd.DataFrame({
    "Height":[150,160,170],
    "Weight":[50,60,70]
})
st.scatter_chart(df,x = "Height",y = "Weight")

#-------------------------------------------------------------------------------------------------------------------------

# PYPLOT
st.write('---------------------------- PYPLOT')

# st.pyplot() # Display Matplotlib figures. Uses - Existing Matplotlib projects, Scientific graphs

# Eg - 
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1,2,3],[3,5,7])
st.pyplot(fig)

#-------------------------------------------------------------------------------------------------------------------------