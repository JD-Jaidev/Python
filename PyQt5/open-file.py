# Open File Dialog in PyQt5

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
        self.button.clicked.connect(self.open_file)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "Text Files (*.txt)"
        )
        if filename:
            with open(filename, "r") as file:
                self.text.setPlainText(file.read())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

'''

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