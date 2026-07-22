# validators in PyQt5

# 1. QIntValidator() - it only allows numbers to be entered

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QIntValidator

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()
phone = QLineEdit()

# Allow numbers from 0 to 2147483647 (final last value avlb)
validator = QIntValidator(0, 2147483647)

phone.setValidator(validator)
phone.setPlaceholderText("Enter Phone Number")

layout.addWidget(phone)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
# -----------------------------------------------------------------------------------------------

# 2. QDoubleValidator() - used for decimal numbers

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QDoubleValidator

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDoubleValidator Example")
        layout = QVBoxLayout()
        self.label = QLabel("Enter a decimal number")
        self.line_edit = QLineEdit()
        # Minimum = 0.0
        # Maximum = 100.0
        # Decimal Places = 2
        validator = QDoubleValidator(0.0, 100.0, 2)
        self.line_edit.setValidator(validator)
        self.line_edit.textChanged.connect(self.show_text)
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

    def show_text(self, text):
        self.label.setText("Value : " + text)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
# -----------------------------------------------------------------------------------------------

# 3. QRegularExpressionValidator

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtCore import QRegularExpression

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()
phone = QLineEdit()
regex = QRegularExpression("[0-9]{10}")
validator = QRegularExpressionValidator(regex)

phone.setValidator(validator)
phone.setPlaceholderText("Enter 10-digit Mobile Number")

layout.addWidget(phone)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())