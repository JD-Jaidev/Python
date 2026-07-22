# creating a secondary window in PyQt5

# In PyQt5, there are three common ways to create another window:
# -----------------------------------------------------------------------------------
# 1. Open a second window while keeping the first window open.
# 2. Switch from one window to another (hide/close the first window).
# 3. Use a QStackedWidget to switch between multiple pages in a single window. (Recommended for multi-page applications.)

# -----------------------------------------------------------------------------------------------------
# 1. open a secondary window

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        layout = QVBoxLayout()
        label = QLabel("Welcome to the Second Window!")
        layout.addWidget(label)
        self.setLayout(layout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        layout = QVBoxLayout()
        button = QPushButton("Open Second Window")
        button.clicked.connect(self.open_second)
        layout.addWidget(button)
        self.setLayout(layout)

    def open_second(self):
        self.second = SecondWindow()   # Create window
        self.second.show()             # Display window


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

# -----------------------------------------------------------------------------------------------------
# 2. switching to secondary window

import sys
from PyQt5.QtWidgets import *

class SecondWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        layout = QVBoxLayout()
        label = QLabel("This is Window 2")
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window 1")
        layout = QVBoxLayout()
        button = QPushButton("Go to Window 2")
        button.clicked.connect(self.switch)
        layout.addWidget(button)
        self.setLayout(layout)

    def switch(self):
        self.second = SecondWindow()
        self.second.show()
        self.close()          # or self.hide()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

# -----------------------------------------------------------------------------------------------------
# 3. going back to the first window

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        button = QPushButton("Go to Second Window")
        button.clicked.connect(self.open_second)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is the Main Window"))
        layout.addWidget(button)
        self.setLayout(layout)

    def open_second(self):
        # Pass the current window (self) to the second window
        self.second = SecondWindow(self)
        self.second.show()

        # Hide the first window
        self.hide()

class SecondWindow(QWidget):
    def __init__(self, first_window):
        super().__init__()

        # Store the first window
        self.first_window = first_window
        self.setWindowTitle("Second Window")

        button = QPushButton("Back")
        button.clicked.connect(self.go_back)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is the Second Window"))
        layout.addWidget(button)

        self.setLayout(layout)

    def go_back(self):
        # Show the first window again
        self.first_window.show()

        # Close this window
        self.close()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())