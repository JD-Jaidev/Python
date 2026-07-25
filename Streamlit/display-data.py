import streamlit as st
import pandas as pd

df = pd.DataFrame({'Fruits' : ['Mango','Banana','Apple']}) # pandas dataframe
st.write(df) # to write dataframe
#st.dataframe(df) same as write tag

st.write('This is a table')
st.table(df) # it gives out a table output similar to the pandas dataframe, but we cannot interactively select as we do in pandas dataframe.