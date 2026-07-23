# Open File Dialog & Save File Dialog in PyQt5

import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Open File Example")
        self.resize(500, 400)
        self.text = QTextEdit()
        self.button = QPushButton("Open File")
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.text)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.button.clicked.connect(self.save_file)

    def open_file(self): # open file dialog
        filename, _ = QFileDialog.getOpenFileName(
            self, # parent
            "Open File", # title
            "", # dir (current dir)
            "Text Files (*.txt)" # filter type
        )
        if filename:
            with open(filename, "r") as file: # readingg contents from file
                self.text.setPlainText(file.read()) # Reads all the text from the file. Displays that text inside the QTextEdit widget.

    def save_file(self): # save file dialog
        filename, _ = QFileDialog.getSaveFileName(
            self, # parent
            "Save File", # title
            "", # current dir
            "Text Files (*.txt)" # save as file type
        )
        if filename:
            with open(filename, "w") as file: # write contents into file
                file.write(self.text.toPlainText()) # Takes the text currently inside the QTextEdit. Writes that text into the file.
                                                    # toPlainText() is another QTextEdit method.
                                                    # It retrieves all the text from the QTextEdit.
                                                    # Returns it as a string.

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

'''
# Example code - 

# Parameters - 
QFileDialog.getOpenFileName(
    parent,
    title,
    starting_folder,
    filter)
    
# Eg - 
    filename, filter = QFileDialog.getOpenFileName(

    self, - # parent
    "Open File", - # text display
    "", - # open which directory(current dir)
    "Text Files (*.txt);;Python Files (*.py);;All Files (*)" - # types of files to filter out

)
print(filename)

# selecting multiple files
files, filter = QFileDialog.getOpenFileNames(
    self,
    "Select Files",
    "",
    "Images (*.png *.jpg)"
)

print(files)

'''

