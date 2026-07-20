import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, # initializes the application and the window
                            QWidget, QVBoxLayout, # vr box layoout
                            QHBoxLayout, # hr box layout
                            QGridLayout) # grid layout, these are layout manager classes 

from PyQt5.QtGui import QIcon, QFont, QPixmap # QIcon for icon objects, OFont to change fonts, QPixmap to load images.

from PyQt5.QtCore import Qt # Qt for alignment control

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layout Managers')
        self.setGeometry(100,100,500,500)
        self.initUI() # initialize the initUI (calls another func to keep constructor clean)

    # we cant directly create a layout manager. so we need tocreate a widget, then add a layout manager to that widget and then add that widget
    # to the main window

    def initUI(self):
        central_widget = QWidget() # we add the layout manager to the central_widget
        self.setCentralWidget(central_widget) # then we add the central widget to the main window (places wudget inside the window)

        label1 = QLabel('NO. 1') # creating labels
        label2 = QLabel('NO. 2')
        label3 = QLabel('NO. 3')
        label4 = QLabel('NO. 4')
        label5 = QLabel('NO. 5')

        label1.setStyleSheet('background-color : red;') # adding bg colors like using css
        label2.setStyleSheet('background-color : green;')
        label3.setStyleSheet('background-color : yellow;')
        label4.setStyleSheet('background-color : blue;')
        label5.setStyleSheet('background-color : purple;')

        vbox = QVBoxLayout() # creates vertical box layout

        vbox.addWidget(label1) # adds label to layout
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox) # assigns vertical layout to central widget

        hbox = QHBoxLayout() # creates horizontal box layout

        hbox.addWidget(label1) # adds label to layout
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)

        central_widget.setLayout(hbox) # assigns horizontal layout to central widget

        grid = QGridLayout() # creates a grid layout

        grid.addWidget(label1,0,0) #(row,column), for eg - (0,0) means 1st row and 1st column
        grid.addWidget(label2,1,0)
        grid.addWidget(label3,2,0)
        grid.addWidget(label4,1,2)
        grid.addWidget(label5,2,1)

        central_widget.setLayout(grid) # adds grid to central widget

def main():
    app = QApplication(sys.argv) # creates application
    window = MainWindow() # creates main window
    window.show() # displays it
    sys.exit(app.exec_()) # starts the event loop. When the user closes the window, app.exec_() returns, and sys.exit() exits the program cleanly.

if __name__ == '__main__': # checks if program is run directly
    main()