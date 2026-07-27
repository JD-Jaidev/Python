# FORMS IN STREAMLIT

import streamlit as st

st.form() # Groups several widgets together. The widgets are processed only when the user clicks the submit button. Without a form, every widget interaction reruns the app immediately.

with st.form(
    key = 1,
    clear_on_submit = False,
    border = True
):
    pass

'''

Parameter	-  Description
key	-  Unique form ID
clear_on_submit	-  Clears fields after submission
border	-  Show form border

'''

# Eg - 
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type = "password"
    )
    submit = st.form_submit_button("Login")
if submit:
    st.success("Login Successful")

#-------------------------------------------------------------------------------------------------------------------------

# FORM SUBMIT BUTTON

st.form_submit_button() # Submits the form. Must be placed inside st.form()

st.form_submit_button(
    label = "Submit",
    help = None,
    on_click = None,
    args = None,
    kwargs = None,
    type = "secondary",
    disabled = False
)

with st.form("student"):
    name = st.text_input("Name")
    age = st.number_input("Age")
    submit = st.form_submit_button(
        "Register"
    )
if submit:
    st.success("Registered!")

#-------------------------------------------------------------------------------------------------------------------------