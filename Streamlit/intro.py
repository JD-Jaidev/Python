import streamlit as st

st.title('First Streamlit program.') # title in the web page like h1
st.write('This a text.') # similar to paragraph tag
st.header('Streamlit') # similar to h2
st.subheader('Tutorial') # similar to h3
st.text('Text tag') # similar to write tag and paragraph tag
st.markdown('Bold text') # it appears like bold text
st.caption('Caption tag') # caption tag (smaller than text tag)
st.code("print('Hello')",language = 'python') # code snippet with ang specified
st.latex("E = mc^2") # centerd italic formula
