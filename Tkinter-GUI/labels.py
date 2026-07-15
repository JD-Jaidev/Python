# LABELS IN TKINTER - AN AREA WIDGET THAT CONTAINS AND/OR IMAGE WITHIN A WINDOW

from tkinter import *

window = Tk()
window.geometry('900x900')

photo = PhotoImage(file = "C:\\Users\\Jaidev\\Downloads\\profile-pic.png")

label =Label(window,
             text = 'hello world', # TEXT INSIDE LABEL
             font = ('Arial',100,'bold'), # FONT (NAME , SIZE , STYLE)
             fg = 'green', # FORE GROUND COLOR (TEXT COLOR)
             bg = 'black', # BG COLOR
             relief = RAISED, # BORDER STYLE (FLAT, RAISED, SUNKEN, RIDGE, GROOVE, SOLID)
             bd = 1, # BORDER WIDTH
             padx = 10, # PADDING X
             pady = 10, # PADDING Y
             image = photo, # ADDING IMAGE
             compound = 'right', # BOTH TEXT AND IMAGE SHOULD EXISTS. SHOWS PLACE WHERE IMAGE SHOULD EXIST.
             width = 420, # LABEL WIDTH
             height = 420, # A=LABEL HEIGHT
             anchor = 'w', # ALIGNS TEXT INSIDE LABEL (n, e, w, s, ne, nw, se, sw, center)
             justify = 'left', # ALIGNS MULTIPLE LINES OF TEXT (left, center, right)
             state = 'disabled', # STATE OF LABEL (normal)
             cursor = 'hand2') # MOUSE CURSOR ICON (arrow, hand2, cross, watch)

label.place(x= 100,y = 100) # PLACES LABEL IN DESIRED PLACE ACC.
label.pack() # DISPLAYS LABEL

window.mainloop()