# USER INPUT WIDGETS - User input widgets allow users to enter data into your Streamlit application. Most of these widgets return a value, which you can store in a variable and use later.

import streamlit as st

#----------------------------------------------------------------------------------------------------------------------
# TEXT INPUT
st.text_input('Enter text') # Accepts a single line of text from the user.
st.text_input(
    label = 'Name',
    value = "",
    max_chars = None,
    key = None,
    type = "default",
    help = None,
    autocomplete = None,
    placeholder = 'Enter name',
    disabled = False,
    label_visibility = "visible"
)
'''

Parameter	-  Description
--------------------------------------------------------
label	-  Text displayed above the input box (Required)
value	-  Default value
placeholder	-  Hint text inside the box
max_chars	-  Maximum allowed characters
type	-  "default" or "password"
help	-  Tooltip
disabled	-  Disable the widget

'''

# Eg - 
name = st.text_input(
    "Enter Your Name",
    placeholder="Type here...",
    type = 'password')
st.write("Hello,", name)

#----------------------------------------------------------------------------------------------------------------------
# TEXT AREA

st.text_area('Enter description') # Accepts multiple lines of text.

st.text_area(
    label = 'Text Area',
    value = "",
    height = None,
    max_chars = None,
    placeholder = None,
    help = None,
    disabled = False
)

# Eg - 
feedback = st.text_area(
    "Feedback",
    placeholder="Enter your feedback..."
)
st.write(feedback)

#----------------------------------------------------------------------------------------------------------------------
# CHAT INPUT

st.chat_input() # Creates a chat input box, commonly used in AI chatbot apps.

st.chat_input(
    placeholder = "Message",
    max_chars = None,
    disabled = False
)

# Eg -
message = st.chat_input("Ask me anything...")
if message:
    st.write("You said:", message)

#----------------------------------------------------------------------------------------------------------------------
# NUMBER INPUT

st.number_input('Enter number input') # Accepts only numerical values.

st.number_input(
    label = 'Enter number',
    min_value = None,
    max_value = None,
    value = None,
    step = None,
    format = None,
    help = None,
    disabled = False
)

# Eg -
age = st.number_input(
    "Age",
    min_value = 1,
    max_value = 100,
    value = 18
)
st.write(age)

#----------------------------------------------------------------------------------------------------------------------
# SLIDER

st.slider('Number selector') # Lets the user select a value using a slider.

st.slider(
    label = 'Mark selector',
    min_value = 10,
    max_value = 100,
    value = None,
    step = 1,
    format = None
)

# Eg - 
age = st.slider(
    "Select Age",
    0,
    100,
    25,
    10
)
st.write(age)

#----------------------------------------------------------------------------------------------------------------------
# SELECT SLIDER

#st.select_slider() #Slider with custom values instead of numbers.

st.select_slider(
    label = 'Fruits',
    options = ['Apple','Mango','Orange'],
    value = None
)

# Eg - 
size = st.select_slider(
    "T-Shirt Size",
    options = ["XS","S","M","L","XL"]
)
st.write(size)

#----------------------------------------------------------------------------------------------------------------------
# CHECKBOX

st.checkbox('YES OR NO') # Allows the user to select True or False.

st.checkbox(
    label = 'Do you like food?',
    value = False,
    help = None,
    disabled = False
)

# Eg - 
agree = st.checkbox(
    "I Agree to Terms"
)
st.write(agree)

#----------------------------------------------------------------------------------------------------------------------
# TOGGLE

st.toggle('Do you like to code?') # Modern ON/OFF switch.

st.toggle(
    label = 'Toggle it',
    value = False
)

# Eg - 
dark = st.toggle(
    "Dark Mode"
)
st.write(dark)

#----------------------------------------------------------------------------------------------------------------------
# RADIO

st.radio('Do you have laptop?',['YES','NO']) # Choose one option from multiple choices.

st.radio(
    label = 'Veggies',
    options = ['Carrot','Potato','Tomato'],
    index = 0,
    horizontal = False # orientation
)

# Eg - 
st.radio(
    "Language",
    ["Python","Java","C++"],
    horizontal = True
)

#----------------------------------------------------------------------------------------------------------------------
# SELECT BOX

st.selectbox('Cars',['BMW','AUDI','TATA']) # Dropdown menu for selecting one option.

st.selectbox(
    label = 'Laptop',
    options = ['Dell','Lenovo','Asus'],
    index = 2 # default selection
)

# Eg - 
country = st.selectbox(
    "Country",
    ["India","USA","Japan"]
)
st.write(country)

#----------------------------------------------------------------------------------------------------------------------
# MULTI SELECT

st.multiselect('Your interest',['Cars','Bikes','Trains']) # Allows selecting multiple options.

st.multiselect(
    label = 'Liked foods',
    options = ['Pizza','Burger','Coke'],
    default = None
)

# Eg -
skills = st.multiselect(
    "Coding skills",
    ["Python","Java","SQL","C++"]
)
st.write(skills)

#----------------------------------------------------------------------------------------------------------------------
# PILLS

st.pills('College name',['MIT','CIT']) # Displays options as clickable pill-shaped buttons.

st.pills(
    label = 'School',
    options = ['EBZN','EBZN MAT'],
    default = 'EBZN'
)

# Eg - 
course = st.pills(
    "Course",
    ["AI","ML","DS"]
)
st.write(course)

#----------------------------------------------------------------------------------------------------------------------
# SEGMENTED CONTROL

st.segmented_control('Subjects',['Mat','Eng','Sci']) # Displays options as connected segments.

st.segmented_control(
    label = 'Cars',
    options = ['BMW','AUDI','VOLVO'],
    default = 'AUDI'
)

# Eg - 
theme = st.segmented_control(
    "Theme",
    ["Light","Dark"]
)
st.write(theme)

#----------------------------------------------------------------------------------------------------------------------
# DATE INPUT

st.date_input() # Lets the user select a date.

st.date_input(
    label = 'Date today',
    value = "today",
    min_value = None,
    max_value = None
)

# Eg - 
dob = st.date_input(
    "Date of Birth"
)

st.write(dob)

#----------------------------------------------------------------------------------------------------------------------
# TIME INPUT

#st.time_input() # Lets the user select a time.

st.time_input(
    label = 'Select time',
    value = None
)

# Eg - 
meeting = st.time_input(
    "Meeting Time"
)
st.write(meeting)

#----------------------------------------------------------------------------------------------------------------------
# COLOR PICKER

#st.color_picker() # Allows the user to choose a color.

st.color_picker(
    label = 'Color picker',
    value = "#000000" # default starting
)

# Eg -
color = st.color_picker(
    "Choose Color"
)
st.write(color)

#----------------------------------------------------------------------------------------------------------------------