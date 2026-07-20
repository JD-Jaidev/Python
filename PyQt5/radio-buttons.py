import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Radio Buttons')
        self.setGeometry(100,100,500,500)
        self.radio1 = QRadioButton('Visa',self) # creating radio buttons
        self.radio2 = QRadioButton('MasterCard',self)
        self.radio3 = QRadioButton('PayPal',self)
        self.radio4 = QRadioButton('In-store',self)
        self.radio5 = QRadioButton('Online',self)
        self.button_group1 = QButtonGroup(self) # creating button groups to as to grp buttons of same/diff kinds
        self.button_group2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0,0,300,50) # sets geometry of radio button
        self.radio2.setGeometry(0,50,300,50)
        self.radio3.setGeometry(0,100,300,50)
        self.radio4.setGeometry(0,150,300,50)
        self.radio5.setGeometry(0,200,300,50)

        self.setStyleSheet('QRadioButton{ font-size : 40px; font-family : Arial; }') # styles radio buttons

        self.button_group1.addButton(self.radio1) # adds similar buttons to group 1
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4) # adds another set of similar buttons to group 2. So that one button from each group can be selected
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed) # if radio buttons are toggled, perform the desired function
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender() # gets the button name (which button)
        if radio_button.isChecked(): # checks if that selected button is checked
            print(f'{radio_button.text()} is selected')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

# .buttons() - gives all the buttons in the a particular group 
# addButton(button) - Adds a button to the group	None
# buttons()	Returns - all buttons in the group	List of buttons
# checkedButton() - Returns the selected button	QRadioButton or None
# checkedId() - Returns the ID of the selected button	Integer
# id(button) - Returns the ID of a given button	Integer
# button(id) - Returns the button with a given ID	QRadioButton
# removeButton(button) - Removes a button from the group	None

'''

Signal	|  When emitted
clicked()	-  User clicks the radio button.
toggled(bool)	-  Selection state changes (True/False).
pressed()	-  Mouse pressed.
released()	-  Mouse released.

'''