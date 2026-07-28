import streamlit as st

# IMAGE
st.write('------------------------------ IMAGE')

# st.image() # Displays one or more images.

'''

st.image(
    image,
    caption = None,
    width = None,
    use_container_width = False,
    channels = "RGB"
)

Parameter	-  Description
image	-  Image path, URL, NumPy array, or PIL image (Required)
caption	-  Image caption
width	-  Image width in pixels
use_container_width	-  Fill the container width
channels	-  "RGB" or "BGR"

'''

# Eg -
st.image(
    "B:\\VoltEdge PC\\assets\\title-icon.png",
    caption = "Cute Cat",
    width = 300
)

#-------------------------------------------------------------------------------------------------------------------------

# AUDIO
st.write('------------------------------ AUDIO')

# st.audio() # Displays an audio player. Uses - Music, Podcasts, Voice recordings

'''

st.audio(
    data,
    format = "audio/wav",
    start_time = 0,
    loop = False,
    autoplay = False
)

st.audio("song.mp3")

'''

#-------------------------------------------------------------------------------------------------------------------------

# VIDEO
st.write('------------------------------ VIDEO')

# st.video # Displays a video player.

'''

st.video(
    data = '<data to be played>',
    start_time = 0,
    subtitles = None,
    autoplay = False,
    loop = False,
    muted = False
)

st.video("movie.mp4")

'''

#-------------------------------------------------------------------------------------------------------------------------

# LOGO
st.write('------------------------------ LOGO')

# st.logo() # Displays your application's logo.

'''

st.logo(
    image,
    icon_image = None,
    link = None
)

'''

# Eg - 
st.logo("B:\\VoltEdge PC\\assets\\title-icon.png")

#-------------------------------------------------------------------------------------------------------------------------

# CONTAINER
st.write('------------------------------ CONTAINER')

# st.container() # Groups widgets together.

'''

container = st.container(
    border = False,
    height = None
)

'''

# Eg - 
with st.container():
    st.header("Student Details")
    st.write("Name: Jaidev")

#-------------------------------------------------------------------------------------------------------------------------

# COLUMNS
st.write('------------------------------ COLUMNS')

# st.columns() # Creates columns for side-by-side layouts.

'''

st.columns(
    spec,
    gap = "small",
    vertical_alignment = "top"
)

Parameter	-  Description
spec	-  Number of columns or relative widths
gap	-  "small", "medium", "large"
vertical_alignment	-  "top", "center", "bottom"

'''

# Eg - 
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
    st.write('HELLO')
with col2:
    st.write("Column 2")
    st.write('WORLD')

# col1, col2 = st.columns([2,1]) # Column 1 will be twice as wide as Column 2.

#-------------------------------------------------------------------------------------------------------------------------

# TABS
st.write('------------------------------ TABS')

# st.tabs() # Creates tabbed pages.

'''

tab1, tab2 = st.tabs([
    "Home",
    "About"
])

'''

# Eg - 
tab1, tab2 = st.tabs(["Python","Java"])
with tab1:
    st.write("Python Course")
    st.write('Python coding...')
with tab2:
    st.write("Java Course")
    st.write('Java coding...')

#-------------------------------------------------------------------------------------------------------------------------

# EXPANDER
st.write('------------------------------ EXPANDER')

# st.expander() # Creates a collapsible section.

'''

with st.expander(
    label,
    expanded = False
):

'''

# Eg -
with st.expander("Show Details"):
    st.write("Student Information")

#-------------------------------------------------------------------------------------------------------------------------

# SIDEBAR
st.write('------------------------------ SIDEBAR')

# st.sidebar() # Creates a permanent sidebar.

# Eg - 
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose",
    ["Home","About"]
)

#-------------------------------------------------------------------------------------------------------------------------

# POPOVER
st.write('------------------------------ POPOVER')

# st.popover() # Displays content inside a popover that appears when clicked.

# Eg -
with st.popover("Settings"):
    st.checkbox("Dark Mode")
    st.slider("Volume",0,100)

#-------------------------------------------------------------------------------------------------------------------------

# DIALOG
st.write('------------------------------ DIALOG')

# st.dialog() # Creates a modal dialog window.

# Eg -
@st.dialog("Login")
def login():
    st.text_input("Username")
    st.button("Login")

if st.button("Open Login"):
    login()

#-------------------------------------------------------------------------------------------------------------------------

# FRAGMENT
st.write('------------------------------ FRAGMENT')

# st.fragment() # Allows part of your app to rerun independently. Useful for improving performance.

# Eg -
if "count" not in st.session_state:
    st.session_state.count = 0

@st.fragment
def counter():
    if st.button("Increment1"):
        st.session_state.count += 1

    st.write("Count:", st.session_state.count)

counter()

#-------------------------------------------------------------------------------------------------------------------------

# SESSION STATE
st.write('------------------------------ SESSION STATE')

# st.session_state() # Stores variables between reruns.

# Eg - 
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(st.session_state.count)

#-------------------------------------------------------------------------------------------------------------------------

# ECHO
st.write('------------------------------ ECHO')

# st.echo() # Displays the Python code being executed. Useful for tutorials.

# Eg -
with st.echo():
    x = 10
    print(x)

#-------------------------------------------------------------------------------------------------------------------------

# HELP
st.write('------------------------------ HELP')

# st.help() # Displays documentation for Python objects.

# Eg -
import math
st.help(math.sqrt)

#-------------------------------------------------------------------------------------------------------------------------

# QUERY PARAMS
st.write('------------------------------ QUERY PARAMS')

# st.query_params() # st.query_params is a dictionary-like object that allows you to read, add, update, or remove URL query parameters.
# Uses - Share app state through the URL, Bookmark specific pages, Save search filters, Pass information between pages

# Eg -
# Set query parameters
st.query_params["name"] = "Jaidev"
st.query_params["course"] = "AIML"

# Read query parameters
st.write("Name:", st.query_params["name"])
st.write("Course:", st.query_params["course"])

#-------------------------------------------------------------------------------------------------------------------------

# SWITCH PAGE
st.write('------------------------------ SWITCH PAGE')

# st.switch_page() # st.switch_page() is used to navigate from one Streamlit page to another in a multipage app.
                    # Instead of clicking the sidebar manually, your code changes the page.

# Eg - 
st.title("Home")

if st.button("Go to About"):
    st.switch_page("pages/About.py")

#-------------------------------------------------------------------------------------------------------------------------

# RERUN
st.write('------------------------------ RERUN')

# st.rerun() # st.rerun() immediately restarts the Streamlit script from the beginning. It stops the current execution and reruns the app.
# Uses - Refresh the page after updating data, Refresh after login/logout, Reload UI after changing session state, Restart the app after a major change

# Eg -
if "count" not in st.session_state:
    st.session_state.count = 0

st.write("Counter:", st.session_state.count)

if st.button("Increment2"):
    st.session_state.count += 1
    st.rerun()

#-------------------------------------------------------------------------------------------------------------------------

# STOP
st.write('------------------------------ STOP')

# st.stop() # st.stop() immediately stops the execution of the Streamlit script.
            # Anything written after st.stop() is not executed.
            # Unlike st.rerun(), it does not restart the app.

# Eg - 
name = st.text_input("Enter your name")

if name == "":
    st.warning("Please enter your name.")
    st.stop()

st.success(f"Welcome {name}")

#-------------------------------------------------------------------------------------------------------------------------

