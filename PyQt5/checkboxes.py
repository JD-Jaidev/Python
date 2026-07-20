import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Checkboxes')
        self.setGeometry(100,100,500,500)
        self.checkbox = QCheckBox('Do you like food ?',self) # creates checkbox
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(0,0,500,100) # sets checkbox geometry
        self.checkbox.setStyleSheet('font-size : 30px;'
                                    'font-family : Arial;') # styles checkbox
        self.checkbox.stateChanged.connect(self.checkbox_changed) # signal - to find state of it, if checkbox is checked or not
                                                                    # use the connect() to connect the signal to a func
    def checkbox_changed(self,state): # this is called the slot func which is automatically called by PyQt5. The state value come from the signal.
                                        # the slot function runs when a signla is emitted
        if state == Qt.Checked: # state of chekbox
            print('You like food')
        else:
            print('You dont like food')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

'''
    
Signal	|  When emitted
clicked()	-  Checkbox clicked.
toggled(bool)	-  Checked/Unchecked state changes.
stateChanged(int)	-  Emits the checkbox state as an integer.
pressed()	-  Mouse pressed.
released()	-  Mouse released.
    
'''