import sys # imports python's built in sys module
from PyQt5.QtWidgets import QApplication, QMainWindow # imports two classes from the Qtwidgets module. QApplication - creates and manages the application.
from PyQt5.QtGui import QIcon # import QIcon class

# QApplication manages the whole application.
# QMainWindow is one window inside that application.
# Widgets like labels and buttons are children of the window.

class MainWindow(QMainWindow): # new class called new window which inherits features QMainWindow 
    def __init__(self): # constructor method - automatically runs whenver you create an object
        super().__init__() # calls the constructor of the parent class - QMainWindow (this initializes the built in functions of the QMainWindow)
        self.setWindowTitle('Simple Window') # sets the title of the window
        self.setGeometry(100,300,500,500) # sets the geometry of the window in (x,y,width,height). width and height of the window. 
                                            # x = particular x pos to place window
                                            #  y = particular y pos to place window 
        self.setWindowIcon(QIcon("C:\\Users\\Jaidev\\Downloads\\profile-pic.png")) # QIcon class is used to create icon objects from image files.

def main():
    app = QApplication(sys.argv) # creates application's main object and initializes Qt, sys.argv - command line arguments
    window = MainWindow() # creates an object of your main window class. [during this python automatically calls the __init__()]
    window.show() # makes the window visible
    sys.exit(app.exec_()) # sys.exit() - closes the application properly, app.exec_() - starts Qt's event loop. without the event loop the window opens & closes immediately.

if __name__ == '__main__': # checks the file is run directly. if the file is imported into another program, then main will not run.
    main() # calls the main func.