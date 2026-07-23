# like its a widget and also acts as an method to give time, used to select time

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTimeEdit
from PyQt5.QtCore import QTime


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTimeEdit")
        layout = QVBoxLayout()
        self.label = QLabel()
        self.time_edit = QTimeEdit()

# i have done this without using the initUI method

        # Methods
        self.time_edit.setTime(QTime.currentTime())
        self.time_edit.setDisplayFormat("hh:mm:ss")
        self.time_edit.setMinimumTime(QTime(9, 0, 0))
        self.time_edit.setMaximumTime(QTime(18, 0, 0))

        # Signals
        self.time_edit.timeChanged.connect(self.time_changed)
        self.time_edit.editingFinished.connect(self.finished)

        layout.addWidget(self.time_edit)
        layout.addWidget(self.label)

        self.setLayout(layout)

    # Slot
    def time_changed(self, time):
        self.label.setText("Selected Time : " + time.toString("hh:mm:ss"))
        print("Time Changed")

    # Slot
    def finished(self):
        print("Editing Finished")


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec_())

'''

QTimeEdit Methods

Method	-  Description
----------------------------------------------------------------------------------
setTime(QTime)	-  Sets the current time.
time()	-  Returns the selected time.
setMinimumTime(QTime)	-  Sets the minimum selectable time.
minimumTime()	-  Returns the minimum time.
setMaximumTime(QTime)	-  Sets the maximum selectable time.
maximumTime()	-  Returns the maximum time.
setTimeRange(QTime, QTime)	-  Sets the minimum and maximum times.
setDisplayFormat(str)	-  Sets the display format of the time.
displayFormat()	-  Returns the current display format.
clear()	-  Clears or resets the editor.

QTimeEdit Signals
----------------------------------------------------------------------------------
Signal	-  Description
timeChanged(QTime)	-  Emitted when the time changes.
dateTimeChanged(QDateTime)	-  Emitted when the internal date/time changes.
editingFinished()	-  Emitted when editing is completed.

'''