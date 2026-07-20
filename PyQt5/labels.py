import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel # used to add labels that contains text or images.
from PyQt5.QtGui import QFont # to change fonts of labels
from PyQt5.QtCore import Qt # sets alignment 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Labels')
        self.setGeometry(100,100,500,500)

        label = QLabel('Hello',self) # creates label - QLabel(text,parent). if i am inside MainWindow class then self refers to the parent.
        label.setFont(QFont('Arial',25)) # changes font and size of font
        label.setGeometry(0,0,500,100) # sets label geometry
        label.setStyleSheet('color : blue;'  # similar to css properties
                             'background-color : black;'
                             'font-weight : bold;'
                             'font-style : italic;')
        
        label.setAlignment(Qt.AlignTop) # aligns vertically top
        label.setAlignment(Qt.AlignBottom) # aligns vertically bottom
        label.setAlignment(Qt.AlignVCenter) # aligns vertically center

        label.setAlignment(Qt.AlignRight) # aligns horizontally right
        label.setAlignment(Qt.AlignLeft) # aligns horizontally left
        label.setAlignment(Qt.AlignHCenter) # aligns horizontally center

        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # using both v and H flags - horizontally center and vertically top 
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # aligns both h an V center
        label.setAlignment(Qt.AlignCenter) # shortcut to place in center

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()