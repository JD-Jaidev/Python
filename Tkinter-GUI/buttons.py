# BUTTONS IN TKINTER - CLICK TO DO STUFF

from tkinter import *

def display():
    print('Button clicked')

window = Tk()

button = Button(window,
             text = 'hello world', # TEXT INSIDE LABEL
             font = ('Arial',100,'bold'), # FONT (NAME , SIZE , STYLE)
             fg = 'green', # FORE GROUND COLOR (TEXT COLOR)
             bg = 'black', # BG COLOR
             activebackground = 'black', # BUTTON COLO STAYS SAME WHEN CLICKED 
             activeforeground = 'green', # BUTTON COLO STAYS SAME WHEN CLICKED 
             #relief = RAISED, # BORDER STYLE (FLAT, RAISED, SUNKEN, RIDGE, GROOVE, SOLID)
             #bd = 1, # BORDER WIDTH
             command = display, # ACTION TO BE PERFORMEd
             padx = 10, # PADDING X
             pady = 10, # PADDING Y
             #image = photo, # ADDING IMAGE
             #compound = 'right', # BOTH TEXT AND IMAGE SHOULD EXISTS. SHOWS PLACE WHERE IMAGE SHOULD EXIST.
             #width = 420, # LABEL WIDTH
             #height = 420, # A=LABEL HEIGHT
             #anchor = 'w', # ALIGNS TEXT INSIDE LABEL (n, e, w, s, ne, nw, se, sw, center)
             #justify = 'left', # ALIGNS MULTIPLE LINES OF TEXT (left, center, right)
             #state = 'disabled', # STATE OF LABEL (normal)
             #cursor = 'hand2') # MOUSE CURSOR ICON (arrow, hand2, cross, watch)
)
button.pack()

window.mainloop() 