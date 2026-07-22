import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ComboBox Example")

        layout = QVBoxLayout()

        self.label = QLabel("Select a Language")

        self.combo = QComboBox()

        # Methods
        self.combo.addItem('SQL') # adds one item
        self.combo.addItems(["Python", "Java", "C++", "JavaScript"]) # adds multiple items
        self.combo.setCurrentIndex(0) # returns the selected item's index
        self.combo.setEditable(True) # is it editable, edits and adds another item in it.

        # Signals
        self.combo.currentIndexChanged.connect(self.index_changed)
        self.combo.currentTextChanged.connect(self.text_changed)
        self.combo.activated.connect(self.activated_item)
        self.combo.highlighted.connect(self.highlighted_item)

        layout.addWidget(self.combo)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def index_changed(self, index):
        print("Index:", index)

    def text_changed(self, text):
        self.label.setText("Selected: " + text)

    def activated_item(self, index):
        print("Activated:", self.combo.itemText(index))

    def highlighted_item(self, index):
        print("Highlighted:", self.combo.itemText(index))

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

'''
# methods - 
----------------------------------------------------------------
Method	-  Purpose
----------------------------------------------------------------
addItem()	-  Add one item
addItems()	-  Add multiple items
currentText()	-  Get selected text
currentIndex()	-  Get selected index
setCurrentIndex()	-  Select by index
setCurrentText()	-  Select by text
count()	-  Number of items
itemText()	-  Get item text by index
removeItem()	-  Remove an item
clear()	-  Remove all items
setEditable()	-  Allow typing
findText()	-  Find an item's index by text

---------------------------------------------------------------------
# signals
---------------------------------------------------------------------
Signal	-  When it is emitted
---------------------------------------------------------------------
currentIndexChanged(int)	-  When the selected index changes
currentTextChanged(str)	-  When the selected text changes
activated(int)	-  When the user selects an item from the drop-down
highlighted(int)	-  When an item is highlighted before selection
---------------------------------------------------------------------

### NOTE
currentIndexChanged() vs activated()
--------------------------------------------------------------------------------------------------------------------------------------------------
A common interview question is the difference between these two signals:

currentIndexChanged() is emitted whenever the current selection changes, whether it was changed by the user or by your code (for example, setCurrentIndex()).
activated() is emitted only when the user actively selects an item from the drop-down list. It is not emitted when your program changes the selection.

This distinction is useful when you want to respond only to user actions and ignore changes made by your code.

'''