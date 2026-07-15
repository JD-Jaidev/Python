# RADIO BUTTON IN TKINTER - SIMILAR TO CHECK BOX BUT YOU CAN SELECT ONLY ONE FROM A GROUP

from tkinter import  * 

def display():
    if x.get() == 1:
        print('YES')
    else:
        print('NO')

window= Tk()

photo = PhotoImage(file = "C:\\Users\\Jaidev\\Downloads\\profile-pic.png")

x = IntVar()
Radiobutton(window,
            text="Option",               # Text
            font=("Arial",20),           # Font
            fg="green",                  # Text color
            bg="black",                  # Background color
            image=photo,                 # Image
            compound="right" ,           # Image + text position
            width=20 ,                   # Width
            height=2,                    # Height
            padx=10,                     # Horizontal padding
            pady=10,                     # Vertical padding
            relief=RAISED,               # Border style
            bd=2,                        # Border width
            cursor="hand2"  ,            # Mouse cursor
            state="normal",              # normal, active, disabled
            command=display,             # Function called on selection
            variable=x ,                 # Shared variable
            value=1 ,                    # Value assigned when selected
            selectcolor="green",         # Color of the selected radio indicator
            activebackground="blue",     # Background while clicking
            activeforeground="white" ,   # Text color while clicking
            anchor="w" ,                 # Position of content
            justify="left"               # Multi-line text alignment
)
Radiobutton(window, text="Python", variable=x, value=1, command=display).pack(anchor="w")
Radiobutton(window, text="Java", variable=x, value=2, command=display).pack(anchor="w")
Radiobutton(window, text="C++", variable=x, value=3, command=display).pack(anchor="w")
Radiobutton(window, text="hello world", variable=x, value=4, command=display).pack(anchor="w")

window.mainloop()