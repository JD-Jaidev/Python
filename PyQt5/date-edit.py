# like its a widget and also acts as an input method to enter date, used to select date

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDateEdit
from PyQt5.QtCore import QDate


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QDateEdit")
        self.label = QLabel()
        self.date_edit = QDateEdit()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setMinimumDate(QDate(2025, 1, 1))
        self.date_edit.setMaximumDate(QDate(2030, 12, 31))
        self.date_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_edit.setCalendarPopup(True)

        # Signals
        self.date_edit.dateChanged.connect(self.date_changed)
        self.date_edit.editingFinished.connect(self.finished)

        layout.addWidget(self.date_edit)
        layout.addWidget(self.label)

        self.setLayout(layout)

    # Slot func1
    def date_changed(self, date):
        self.label.setText("Selected Date : " + date.toString("dd/MM/yyyy"))
        print("Date Changed")

    # Slot func2
    def finished(self):
        print("Editing Finished")


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec_())

'''

QDateEdit Methods

Method	-  Description
----------------------------------------------------------------------------------
setDate(QDate)	-  Sets the current date.
date()	-  Returns the selected date.
setMinimumDate(QDate)	-  Sets the minimum selectable date.
minimumDate()	-  Returns the minimum date.
setMaximumDate(QDate)	-  Sets the maximum selectable date.
maximumDate()	-  Returns the maximum date.
setDateRange(QDate, QDate)	-  Sets the minimum and maximum dates.
setDisplayFormat(str)	-  Sets the display format of the date.
displayFormat()	-  Returns the current display format.
setCalendarPopup(bool)	-  Enables or disables the calendar popup.
calendarPopup()	-  Returns whether the calendar popup is enabled.
clear()	-  Clears or resets the editor.

QDateEdit Signals

Signal	-  Description
----------------------------------------------------------------------------------
dateChanged(QDate)	-  Emitted when the date changes.
dateTimeChanged(QDateTime)	-  Emitted when the internal date/time changes.
editingFinished()	-  Emitted when editing is completed.

'''