import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFormLayout, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Form Layout')
        self.setGeometry(100,100,500,500)
        self.form = QFormLayout(self)
        self.name = QLineEdit(self)
        self.email = QLineEdit(self)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.submit_button = QPushButton('Submit',self)
        self.initUI()

    def initUI(self):
        self.form.addRow(self.name)
        self.form.addRow(self.email)
        self.form.addRow(self.password)
        self.form.addRow(self.submit_button)
        self.setLayout(self.form)

        self.submit_button.setGeometry(0,400,200,200)
        self.name.setGeometry(0,0,200,50)
        self.email.setGeometry(0,100,200,50)
        self.password.setGeometry(0,200,200,50)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

    
'''

# common methods - 
1. .addRow(label,widget)
2. .addRow(widget)
3. .addRow(label,layout)

'''