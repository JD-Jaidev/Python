# FILE DIALOG SAVE IN TKINTER - SAVES A FILE

from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main", # FILE PATH
                                    defaultextension='.txt', # DEFAULT FILE EXTN
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ]) # FILE TYPES
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    #filetext = input("Enter some text I guess: ") //use this if you want to use console window
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()