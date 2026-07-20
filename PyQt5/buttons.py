import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Buttons')
        self.setGeometry(100,100,500,500)
        self.button = QPushButton('Click ME !',self) # (text,parent) 
        self.label = QLabel('Hello',self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet('font-size : 30px;')
        self.button.clicked.connect(self.on_click) # (sig)clicked is a signal. A signal is emitted automatically when the user clicks the button.
                                                   # Connects the signal to a function. 
                                                   # button.clicked.connect(function_name) - general syntax
                                                   # self.button.clicked.connect(self.function_name) - if button is an instance attribute
        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet('font-size : 50px;')

    def on_click(self):
        self.label.setText('GoodBye')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()