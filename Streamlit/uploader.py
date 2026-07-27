import streamlit as st

#st.file_uploader() #Allows users to upload files. Uses PDFs, Images, Excel, CSV, Documents

st.file_uploader(
    label = 'Uploads',
    type = None,
    accept_multiple_files = False,
    help = None,
    disabled = False
)

# Eg - 
uploaded = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)
if uploaded:
    st.success("Uploaded Successfully")


image = st.file_uploader(
"Upload Image",
type=["png","jpg"]
)
if image:
    st.image(image)

#-------------------------------------------------------------------------------------------------------------------------

# CAMERA INPUT

#st.camera_input() # Capture an image using the device camera. Uses Attendance, Face Recognition, ID Verification

st.camera_input(
    label = 'Cameras',
    help = None,
    disabled = False
)

# Eg - 
photo = st.camera_input(
    "Take Photo"
)
if photo:
    st.image(photo)

#-------------------------------------------------------------------------------------------------------------------------

# AUDIO INPUT

st.audio_input() # Record audio directly from the microphone. Uses Voice Notes, Speech Recognition, AI Assistants

st.audio_input(
    label = 'Audios',
    help = None,
    disabled = False
)

# Eg - 
audio = st.audio_input(
    "Record Voice"
)
if audio:
    st.audio(audio)

#-------------------------------------------------------------------------------------------------------------------------

# AUDIO 

st.audio() # st.audio() is used to play audio files directly in your Streamlit app. It displays an audio player with controls like play, pause, seek, and volume.

st.audio(
    data = '<the file>',
    format = "audio/wav",
    start_time = 0,
    end_time = None,
    loop = False,
    autoplay = False
)

'''

Parameter	-  Description
data	-  File path, bytes, URL, or file-like object
format	-  MIME type (e.g., "audio/mp3" or "audio/wav")
start_time	-  Time (in seconds) to begin playback
end_time	-  Time (in seconds) to stop playback
loop	-  Repeat playback continuously
autoplay	-  Start playing automatically (browser support varies)

'''

# Eg - 
st.audio('song.mp3') # Local audio file

# Play from bytes
with open("music.mp3", "rb") as file:
    audio_bytes = file.read()
st.audio(
    audio_bytes,
    format = "audio/mp3"
)

# Play from file
uploaded = st.file_uploader(
    "Upload an audio file",
    type = ["mp3", "wav"],
    start_time = 30, # Start at a specific time
    end_time=45, # Ends at specific part
    loop = True, # Loops
    autoplay = True # Autplays
)
if uploaded:
    st.audio(uploaded)
