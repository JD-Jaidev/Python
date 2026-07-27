# INTRODUCTION TO STREAMLIT - Streamlit is an open-source Python framework used to build interactive web applications entirely using Python. 
# It is especially popular among data scientists, AI/ML engineers, and Python developers because you don't need to learn HTML, CSS, or JavaScript to create a web interface.

# TEXT DISPLAY WIDGETS - These widgets are used to display text, formatted content, code, equations, and important information on your Streamlit app. 

import streamlit as st

st.title('First Streamlit program.') # Displays the main title of your Streamlit application.
st.write('This a text.') # The most versatile display func. It can display almost everything,
                         # Text, variables, dataframes, dictionaries, lists, images, charts.
st.header('Streamlit') # Displays a large section heading.
st.subheader('Tutorial') # Displays a heading smaller than header(). 
st.text('Text tag') # Displays plain text, no markdown, no formatting.
st.markdown('Bold text') # Displays markdown - bold, italic, headers, lists, tables, HTML.
st.caption('Caption tag') # Displays small grey text useful for notes.
st.code("print('Hello')",language = 'python') # Displays syntax highlighted code.
st.latex("E = mc^2") # Displays mathematical equations.
st.html() # Displays custom HTML inside """.
st.json() # Displays json in a readable format.
st.metric() # Shows KPI (Key performance indicator), useful in dashboards.
st.badge('AI',color = 'blue') # Displays a small colored label (badge) to highlight status or categories.

# CHAT MESSAGE

st.chat_message('Chat messages')
with st.chat_message(
    "Jaidev",
    avatar="🧑‍💻"
):
    st.write("Hello!")
with st.chat_message(
    "AI",
    avatar="🤖"
):
    st.write("Welcome!")
