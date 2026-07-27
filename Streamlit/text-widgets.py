# INTRODUCTION TO STREAMLIT - Streamlit is an open-source Python framework used to build interactive web applications entirely using Python. 
# It is especially popular among data scientists, AI/ML engineers, and Python developers because you don't need to learn HTML, CSS, or JavaScript to create a web interface.

# TEXT DISPLAY WIDGETS - These widgets are used to display text, formatted content, code, equations, and important information on your Streamlit app. 

import streamlit as st
import time

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
#st.html() # Displays custom HTML inside """.
#st.json() # Displays json in a readable format.
#st.metric() # Shows KPI (Key performance indicator), useful in dashboards.
st.badge('AI',color = 'blue') # Displays a small colored label (badge) to highlight status or categories.

# CHAT MESSAGE - st.chat_message() is used to create chat bubbles in a Streamlit app. It is mainly used for building AI chatbots (like ChatGPT), customer support bots, or messaging interfaces.
                # It does not collect user input. Instead, it displays messages. User input is typically collected using st.chat_input().

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

#-------------------------------------------------------------------------------------------------------------------------

# WRITE STREAM - st.write_stream() is a Chat Elements widget in Streamlit that displays content gradually as it is generated, rather than showing it all at once. It is commonly used to create a typing effect for AI responses, making chatbots feel more natural and interactive.
                # It accepts a generator, iterator, or streaming response and writes each piece of content to the app as it becomes available.

#st.write_stream()

# Eg1 - 
def response():
    text = "Welcome to Streamlit! This message is streamed word by word."

    for word in text.split():
        yield word + " "
        time.sleep(0.2)


# Eg2 -
st.write_stream(response())

user_prompt = st.chat_input("Ask a question")

if user_prompt:
    with st.chat_message("user"):
        st.write(user_prompt)
    with st.chat_message("Assistant"):

        def ai_response():
            answer = "Python is a high-level programming language used for web development, AI, data science, and automation."
            for word in answer.split():
                yield word + " "
                time.sleep(0.1)
        st.write_stream(ai_response())