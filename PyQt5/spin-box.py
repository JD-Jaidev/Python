import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Spin Box')
        self.setGeometry(100,100,500,500)
        self.spin = QSpinBox(self)
        self.initUI()

    def initUI(self):
        self.spin.setGeometry(0,0,100,100)
        self.spin.setRange(0,3)
        self.spin.setPrefix('Hello')
       

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


'''

Method	-  Description

setMinimum(value)	-  Sets minimum value.
setMaximum(value)	-  Sets maximum value.
setRange(min, max)	-  Sets minimum and maximum values.
setValue(value)	-  Sets current value.
value()	-  Returns current integer value.
setSingleStep(step)	-  Sets increment/decrement step size.
setPrefix(text)	-  Adds text before the number.
setSuffix(text)	-  Adds text after the number.
setReadOnly(True)	Makes the value non-editable.

Signal	-  Description
valueChanged(int)	-  Emitted whenever the value changes.
textChanged(str)	-  Emitted when the displayed text changes.
editingFinished()	-  Emitted after the user finishes editing.

'''