import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Line Edits')
        self.setGeometry(100,100,500,500)
        self.line_edit = QLineEdit(self) # creates a line_edit / input box
        self.button = QPushButton('Submit',self) # creates a push button
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10,10,200,40)
        self.line_edit.setStyleSheet('font-size : 25px; font-family : Arial;')
        self.line_edit.setPlaceholderText('Enter you name') # placeholder text in the input box
        self.button.setGeometry(210,10,100,40)
        self.button.clicked.connect(self.submit) # connects the button to a function if a signal emits 

    def submit(self):
        text = self.line_edit.text() # gets the text from the line_edit / input box
        print(text)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()