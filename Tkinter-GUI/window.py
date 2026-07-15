# WINDOW IN TKINTER - SERVES AS A CONTAINER TO HOLD OR CONTAIN WIDGETS

from tkinter import *

window = Tk() # INITIATE WINDOW

window.geometry('420x420') # CHANGES WINDOW SIZE (WxH)
window.title('Jaidev Program') # CHANGES THE WINDOW TITLE
photo = PhotoImage(file = "C:\\Users\\Jaidev\\Downloads\\profile-pic.png") # CALLING OR LIKE IMPORTING AND IMAGE
window.iconphoto(True,photo) # CHANGES WINDOW ICON
window.config(background = '#00ff00') # CHANGES WINDOW BACKGROUND TO DESIRED COLOR NAME OR HEX CODE 
window.resizable(True,True) # RESIZABLE WINDOW (HR_RESIZING,VR_RESIZING)
window.minsize(500,500) # MINIMUM SIZE
window.maxsize(750,750) # MAXIMUM SIZE

# ATTRIBUTES
window.attributes('-topmost',True) # ALWAYS ON TOP
window.attributes('-fullscreen',True) # ALWAYS FULLSCREEN
window.attributes('-alpha',0.8) # TRANSPARENCY

window.destroy() # CLOSES WINDOW COMPLETELY
window.update() # REFRESHES THE WINDOW IMMEDIATELY

window.mainloop() # CALL OR PRINT WINDOW