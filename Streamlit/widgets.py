'''import streamlit as st

name = st.text_input('Enter your name') # input to enter text
number = st.number_input('Enter your age',min_value = 10 , max_value = 20) # input to enter number with min and max value

rating = st.slider('Enter your rating',0,10,7) # slider widget with min max and default value
select = st.selectbox('Choose your color',['red','green','yellow','blue']) # drop down box with options as list

check1 = st.checkbox('Yes') # checkbox
if check1: # if checked it gives the message in a write tag
    st.write('You checked !')
else:
    st.write('Your not checked')

radio = st.radio('Do you like food?',['YES','NO'])


area = st.text_area('Enter feedback') # text area to enter text
date = st.date_input('Enter date') # data picker
time = st.time_input('Enter time') # time picker
file =st.file_uploader('Upload file') # choose file to upload


st.echo('SHOW')
st.success('Success',icon="✅")
st.info('Info',icon = None)
st.error('Error',icon = None)
st.warning('Warning',icon = None)
st.toast('Toast',icon = None)
st.progress(70)
#st.spinner()
st.status()

import streamlit as st
import time

progress = st.progress(0, text="Uploading file...")

for i in range(101):
    time.sleep(0.05)
    progress.progress(i, text=f"Uploading... {i}%")
    

import streamlit as st
import time

with st.spinner("Loading data..."):
    time.sleep(3)

st.success("Data loaded!")

import streamlit as st
import time

with st.status("Processing...", expanded=True):
    st.write("Reading file...")
    time.sleep(2)

    st.write("Cleaning data...")
    time.sleep(2)

    st.write("Generating report...")
    time.sleep(2)

st.success("Done!")'''

'''

1. Notification Message Widgets

These display messages to inform the user about the result of an action.

Widget	Purpose
st.success()	Show a successful operation
st.info()	Display general information
st.warning()	Warn the user about something
st.error()	Display an error message
st.exception()	Show an exception and traceback

2. Progress & Loading Widgets

These indicate that a task is running or how much has been completed.

Widget	Purpose
st.progress()	Shows percentage/progress bar
st.spinner()	Shows a loading spinner while code runs
st.status()	Displays the status of a multi-step task

3. Temporary Notification Widget

Used for short-lived notifications.

Widget	Purpose
st.toast()	Small notification that disappears automatically

4. Placeholder Widget

Used to reserve space that you can update later.

Widget	Purpose
st.empty()	Creates an empty placeholder

5. Logging / Debugging Widgets

Useful while developing and debugging your application.

Widget	Purpose
st.echo()	Displays the code being executed
st.help()	Shows documentation for an object
st.exception()	Displays detailed exception information

Complete Classification of Text Display Widgets
A. Headings
st.title()
st.header()
st.subheader()

B. Text Display
st.text()
st.write()
st.markdown()
st.caption()

C. Formatted Content
st.code()
st.latex()
st.html()
st.json()

D. Data Summary
st.metric()
st.badge()

E. Notification Messages
st.success()
st.info()
st.warning()
st.error()
st.exception()

F. Progress & Loading
st.progress()
st.spinner()
st.status()

G. Temporary Notification
st.toast()

H. Placeholders
st.empty()

I. Debugging & Documentation
st.help()
st.echo()

'''

import streamlit as st
plc = st.empty()
plc.text('Hello')