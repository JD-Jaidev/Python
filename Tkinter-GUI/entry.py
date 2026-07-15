# ENTRIES IN TKINTER - TEXT BOX THAT ACCEPTS SINGLE LINE OF INPUT

from tkinter import *

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

def submit():
    text = entry.get()
    print(text)

window = Tk()

btn1 = Button(window,
              text = 'delete',
              font  = ('Arial',20),
              fg = 'blue',
              bg = 'grey',
              command = delete
)
btn1.pack()

btn2 = Button(window,
              text = 'backspace',
              font  = ('Arial',20),
              fg = 'blue',
              bg = 'grey',
              command = backspace
)
btn2.pack()

btn3 = Button(window,
              text = 'submit',
              font  = ('Arial',20),
              fg = 'blue',
              bg = 'grey',
              command = submit
)
btn3.pack()

    
entry = Entry(window,
             font = ('Arial',20,'bold'), # FONT (NAME , SIZE , STYLE)
             fg = 'green', # FORE GROUND COLOR (TEXT COLOR)
             bg = 'black', # BG COLOR
             show = '*', # TO HIDE THINGS LIKE PWD
             #relief = RAISED, # BORDER STYLE (FLAT, RAISED, SUNKEN, RIDGE, GROOVE, SOLID)
             #bd = 1, # BORDER WIDTH        
             #justify = 'left', # ALIGNS MULTIPLE LINES OF TEXT (left, center, right)
             #state = 'disabled', # STATE OF LABEL (normal)
             #cursor = 'hand2') # MOUSE CURSOR ICON (arrow, hand2, cross, watch))
)
entry.pack()

window.mainloop()