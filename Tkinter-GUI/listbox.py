# LISTBOX = A LISTING OF SELECTABLE TEXT ITEMS WITHIN IT'S OWN CONTAINER

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

frame = Frame(window)
frame.pack()

submitButton = Button(frame,text="submit",command=submit)
submitButton.pack(side=LEFT)

addButton = Button(frame,text="add",command=add)
addButton.pack(side=LEFT)

deleteButton = Button(frame,text="delete",command=delete)
deleteButton.pack(side=LEFT)

window.mainloop()

'''

listbox.insert(END, "Python")       # Add item
listbox.insert(0, "Java")           # Insert at index 0
listbox.delete(0)                   # Delete first item
listbox.delete(0, END)              # Delete all items
listbox.get(0)                      # Get first item
listbox.get(ACTIVE)                 # Get selected item
listbox.curselection()              # Get selected index/indices
listbox.size()                      # Number of items
listbox.selection_set(0)            # Select first item
listbox.selection_clear(0, END)     # Clear selectio
listbox.activate(2)                 # Make item at index 2 active
listbox.see(END)                    # Scroll to the last item

# ADDING ITEMS
listbox.insert(END, "Python")           # Add item at the end
listbox.insert(0, "Java")               # Insert item at index 0

# DELETING ITEMS
listbox.delete(0)                       # Delete first item
listbox.delete(2)                       # Delete third item
listbox.delete(0, END)                  # Delete all items

# GETTING ITEMS
listbox.get(0)                          # Get first item
listbox.get(END)                        # Get last item
listbox.get(ACTIVE)                     # Get active item

# SELECTION
listbox.curselection()                  # Returns selected index/indices
listbox.selection_set(0)                # Select first item
listbox.selection_clear(0, END)         # Clear all selections

# ACTIVE ITEM
listbox.activate(2)                     # Make index 2 the active item

# SIZE
listbox.size()                          # Number of items in the listbox

# SCROLL
listbox.see(END)                        # Scroll to the last item

# INDEX
listbox.index(ACTIVE)                   # Get index of active item

# NEAREST ITEM
listbox.nearest(y)                      # Returns the index nearest the y-coordinate

'''