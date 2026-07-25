# Boiler plate code in PyQt5. This code structure is the same for every program
# Boilerplate code is pre-written, reusable code that you include at the beginning of a program 
# or file to set up the basic structure before writing the actual logic.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Title')
        self.setGeometry(100,100,500,500)
        self.initUI()

    def initUI(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()