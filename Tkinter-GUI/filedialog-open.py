# FILEDIALOG OPEN IN TKINTER - OPENS FILE DIALOG

from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main", # FILE PATH
                                          title="Open file okay?", # WINDOW TITLE
                                          filetypes= (("text files","*.txt"), # TYPES OF FILES
                                          ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()