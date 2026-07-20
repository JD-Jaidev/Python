import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap # QPixmap is a class in PyQt that is used to load, store, and display images in GUI applications. 
                                # QPixmap loads the image into memory in a format that Qt can display.

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Images') # sets window title
        self.setGeometry(100,100,500,500) # sets window geometry

        label = QLabel(self) # creates label
        label.setGeometry(0,0,250,250) # sets label geometry

        pixmap = QPixmap("C:\\Users\\Jaidev\\Downloads\\profile-pic.png") # loads an image
        label.setPixmap(pixmap) # sets image to label

        label.setScaledContents(True) # resizes/scales image to fit in the label

        label.setGeometry(self.width(), # gets window width (MainWindow)
                            self.height(), # gets window height
                            label.width(), # gets label width
                            label.height()) # gets label height
        
        label.setGeometry(self.width() - label.width(),
                          self.height() - label.height(),
                          label.width(),
                          label.height()) # bottom right

        label.setGeometry(0,
                          self.height() - label.height(),
                          label.width(),
                          label.height()) # bottom left
        
        label.setGeometry(self.width() - label.width(),
                          0,
                          label.width(),
                          label.height()) # top right
        
        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height()) # center

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()