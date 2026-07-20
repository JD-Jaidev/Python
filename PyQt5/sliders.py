import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Slider') # window title 
        self.setGeometry(100,100,500,500) # window geometry
        self.slider = QSlider(Qt.Horizontal,self) # creates slider and gives orientation
        self.button = QPushButton('Value',self) # creates push button
        self.initUI()

    def initUI(self):
        self.slider.setGeometry(20,20,500,40) # sets slider geometry
        self.slider.setRange(0,100) # sets slider range
        self.slider.setMaximum(100) # slider cant go above this value
        self.slider.setMinimum(0) # slider cant go below this value
        self.button.setGeometry(0,100,200,50) # sets button geometery
        self.button.clicked.connect(self.submit) # signal when button clicked
        self.slider.setTickInterval(10) # intervals
        self.slider.setTickPosition(QSlider.TicksLeft) # tick marks position

        '''
    
        QSlider.NoTicks
        QSlider.TicksAbove
        QSlider.TicksBelow
        QSlider.TicksLeft
        QSlider.TicksRight
        QSlider.TicksBothSides
        
        '''

        self.slider.setSingleStep(10) # it sets how much the slider moves when the user presses the keyboard arrow keys (or other fine-grained controls)
        #self.slider.setPageStep(20) # this controls how much the slider moves when the user clicks on the slider's groove (track) away from the handle, or uses the Page Up/Page Down keys.
        self.slider.setInvertedAppearance(False) # inverted range
        self.slider.setEnabled(True) # is slider enabled
        self.slider.valueChanged.connect(self.display) # if value changed

    def submit(self): # slot func when button clicked
        value = self.slider.value()
        print(value)

    def display(self):
        print(self.slider.value())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()