# KEYBOARD EVENTS IN TKINTER - THESE ARE THE EVENTS THAT OCCUR WHEN USER PRESSE OR RELEASES A KEY ON THE KEYBOARD

from tkinter import *

def doSomething(event):
    #print("You pressed: " + event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>",doSomething)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()