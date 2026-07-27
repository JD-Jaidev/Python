# BUTTONS IN STREAMLIT

import streamlit as st
import pandas as pd

#st.button() # When the user clicks it, the button returns True for that run. Uses Submit, Save, Login, Delete, Calculate
def click():
    st.success('Well donee!')

st.button(
    label = 'Button widgets',
    key = 1,
    help = None,
    on_click = click,
    args = None,
    kwargs = None,
    type = "secondary",
    icon = None,
    disabled = False,
    use_container_width = False
)

'''

Parameter	-  Description
label	-  Button text (Required)
key	-  Unique widget ID
help	-  Tooltip
on_click	-  Function called when clicked
args	-  Arguments for the callback function
kwargs	-  Keyword arguments for the callback
type	-  "primary" or "secondary"
icon	-  Emoji or icon
disabled	-  Disable the button
use_container_width	-  Stretch button to container width

'''

# Eg - 
if st.button("Login"):
    st.success("Logged In Successfully!")

st.button(
    "Save",
    type = "primary"
)

st.button(
    "Download",
    icon = "⬇️"
)

#-------------------------------------------------------------------------------------------------------------------------

# DOWNLOAD BUTTON

#st.download_button() # Allows users to download files or data. Use Reports, PDFs, CSV, Excel, Images

st.download_button(
    label = 'Download anything',
    file_name = None,
    mime = None,
    help = None
)

'''

Parameter	-  Description
label	-  Button text
data	-  Data to download
file_name	-  Downloaded file name
mime	-  File type
help	-  Tooltip

'''

# Eg -
text = "Hello Streamlit"

st.download_button(
    "Download",
    data = text,
    file_name = "hello.txt",
    mime = "text/plain"
)

#-------------------------------------------------------------------------------------------------------------------------

# LINK BUTTON

st.link_button('Portfolio','https://jaidev-s-portfolio.web.app/') # Creates a button that opens a web page.

st.link_button(
    label = 'Port',
    url = 'https://jaidev-s-portfolio.web.app/',
    help = None,
    disabled = False
)

# Eg - 
st.link_button(
    "Visit Google",
    "https://google.com"
)

#-------------------------------------------------------------------------------------------------------------------------

# PAGE LINK 
st.page_link() # Navigate to another page inside a multipage Streamlit app. 

st.page_link(
    page = 'https://jaidev-s-portfolio.web.app/',
    label = None,
    icon = '📈',
    disabled = False
)

# Eg - 
st.page_link(
    "pages/About.py",
    label = "About Us"
)

#-------------------------------------------------------------------------------------------------------------------------