# MESSAGE AND PROGRESS WIDGETS - These widgets help you inform users, display errors, show progress, and indicate that a task is running.

import streamlit as st
import time

st.success('Success',icon = '📈') # Displays a green success message.
st.info('Info',icon = '📈') # Displays a blue info message.
st.error('Error',icon = '📈') # Displays a red error message.
st.warning('Warning',icon = '📈') # Displays a yellow warning message.
# st.exception('Exception') # Displays a Python exception with its traceback. Useful while debugging.
st.toast('Hello',icon = '📈') # Displays a small temporary notification. Disappears automatically.
st.progress(75,text = 'Loading') # Shows how much work has been completed.

#----------------------------------------------------------------------------------------------------------------------

# Eg program for progress - 

progress = st.progress(0)
for i in range(101):
    time.sleep(0.05)
    progress.progress(i,text = f'Loading : {i}')

#----------------------------------------------------------------------------------------------------------------------
# SPINNER

st.spinner() # Shows a loading spinner while code is running. Used when you don't know the exact progress percentage. 

# Eg - 
with st.spinner(text="Loading..."):
    time.sleep(3)
st.success('Doneee',icon = '📈')

#----------------------------------------------------------------------------------------------------------------------
# STATUS

st.status('Finished') # Displays the status of a multi-step process. Unlike spinner, it can show each stage of the task.

# Eg - 
with st.status(
    "Processing...",expanded = True):
    st.write("Loading Data...")
    time.sleep(2)
    st.write("Cleaning Data...")
    time.sleep(2)
    st.write("Training Model...")
    time.sleep(2)
st.success("Finished!")

#----------------------------------------------------------------------------------------------------------------------

with st.status(
    "Working...",
    expanded = True
) as status:

    st.write("Loading...")
    time.sleep(2)

    st.write("Saving...")
    time.sleep(2)

    status.update(
        label = "Completed!",
        state = "complete",
        expanded = False
    )

#----------------------------------------------------------------------------------------------------------------------
# EMPTY

st.empty() # Creates an empty placeholder that can later display or replace content.

# Eg - 
placeholder = st.empty()
placeholder.write("Loading...")
time.sleep(2)
placeholder.success("Completed!")

#----------------------------------------------------------------------------------------------------------------------
