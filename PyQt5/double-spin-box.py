# it is used to select decimal/floating point numbersx

import sys
from PyQt5.QtWidgets import *

class Window(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.spin = QDoubleSpinBox()

        self.spin.setRange(0,100) # minimum and maximum values
        self.spin.setDecimals(2) # set decimal places
        self.spin.setSingleStep(0.5) # set increment/decrement amnt
        self.spin.setPrefix("₹ ") # add text before value
        self.spin.setSuffix(" INR") # add text after value
        #setValue()	# Set current value
        #value() # Get current value

        self.spin.valueChanged.connect(self.value_changed)
        self.spin.textChanged.connect(self.text_changed)
        self.spin.editingFinished.connect(self.finished)

        layout.addWidget(self.spin)

        self.setLayout(layout)

    def value_changed(self,value):
        print("Value :",value)

    def text_changed(self,text):
        print("Text :",text)

    def finished(self):
        print("Editing Finished")

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

'''

Signal	-  Purpose
valueChanged(float)	-  Value changes, the float is the type of signal emitted
textChanged(str)	-  Displayed text changes
editingFinished()	-  User finishes editing


'''