from tkinter import  * 

def display():
    if x.get() == 1:
        print('YES')
    else:
        print('NO')

window= Tk()

photo = PhotoImage(file = "C:\\Users\\Jaidev\\Downloads\\profile-pic.png")

x = IntVar()
check_button = Checkbutton(window,
             text = 'hello world', # TEXT INSIDE BUTTON
             font = ('Arial',20,'bold'), # FONT (NAME , SIZE , STYLE)
             fg = 'green', # FORE GROUND COLOR (TEXT COLOR)
             bg = 'black', # BG COLOR
             relief = RAISED, # BORDER STYLE (FLAT, RAISED, SUNKEN, RIDGE, GROOVE, SOLID)
             bd = 1, # BORDER WIDTH
             padx = 10, # PADDING X
             pady = 10, # PADDING Y
             image = photo, # ADDING IMAGE
             compound = 'right', # BOTH TEXT AND IMAGE SHOULD EXISTS. SHOWS PLACE WHERE IMAGE SHOULD EXIST.
             width = 20, # BTN WIDTH
             height = 2, # BTN HEIGHT
             variable = x, # VARIABLE DEFINED
             onvalue = 1, # ON VALUE
             offvalue = 0, # OFF VALUE
             command = display
             #anchor = 'w', # ALIGNS TEXT INSIDE BTN (n, e, w, s, ne, nw, se, sw, center)
             #justify = 'left', # ALIGNS MULTIPLE LINES OF TEXT (left, center, right)
             #state = 'disabled', # STATE OF BTN (normal)
)
check_button.pack()

window.mainloop()