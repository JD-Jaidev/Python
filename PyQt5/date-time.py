import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import QDate, QTime
# QDate and QTime are classes and not widgets

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QDate and QTime Demo")
        self.setGeometry(200, 200, 500, 400)

        layout = QVBoxLayout()

        # ---------------- QDate ----------------
        self.date = QDate.currentDate()

        print("Current Date:", self.date)
        print("Day:", self.date.day())
        print("Month:", self.date.month())
        print("Year:", self.date.year())
        print("Day of Week:", self.date.dayOfWeek())
        print("Day of Year:", self.date.dayOfYear())
        print("Days in Month:", self.date.daysInMonth())
        print("Days in Year:", self.date.daysInYear())
        print("Is Valid:", self.date.isValid())

        print("Default Format:", self.date.toString())
        print("dd/MM/yyyy :", self.date.toString("dd/MM/yyyy"))
        print("MMMM dd yyyy :", self.date.toString("MMMM dd yyyy"))

        print("Add 10 Days :", self.date.addDays(10))
        print("Add 2 Months :", self.date.addMonths(2))
        print("Add 1 Year :", self.date.addYears(1))

        # ---------------- QTime ----------------
        self.time = QTime.currentTime()

        print("\nCurrent Time:", self.time)
        print("Hour:", self.time.hour())
        print("Minute:", self.time.minute())
        print("Second:", self.time.second())
        print("Milliseconds:", self.time.msec())
        print("Is Valid:", self.time.isValid())

        print("Default Format:", self.time.toString())
        print("hh:mm:ss :", self.time.toString("hh:mm:ss"))
        print("hh:mm AP :", self.time.toString("hh:mm AP"))

        print("After 60 Seconds:", self.time.addSecs(60))
        print("After 1000 Milliseconds:", self.time.addMSecs(1000))


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec_())

'''

# QDateTimeEdit Methods

Method	-  Description
----------------------------------------------------------------------------------
setDateTime(QDateTime)	-  Sets both the date and time.
dateTime()	-  Returns the current date and time.
setDate(QDate)	-  Sets only the date.
date()	-  Returns only the date.
setTime(QTime)	-  Sets only the time.
time()	-  Returns only the time.
setMinimumDate(QDate)	-  Sets the minimum selectable date.
setMaximumDate(QDate)	-  Sets the maximum selectable date.
setDateRange(QDate, QDate)	-  Sets the date range.
setMinimumTime(QTime)	-  Sets the minimum selectable time.
setMaximumTime(QTime)	-  Sets the maximum selectable time.
setTimeRange(QTime, QTime)	-  Sets the time range.
setMinimumDateTime(QDateTime)	-  Sets the minimum selectable date and time.
setMaximumDateTime(QDateTime)	-  Sets the maximum selectable date and time.
setDateTimeRange(QDateTime, QDateTime)	-  Sets the minimum and maximum date and time.
setDisplayFormat(str)	-  Sets the display format.
displayFormat()	-  Returns the current display format.
setCalendarPopup(bool)	-  Enables or disables the calendar popup.
calendarPopup()	-  Returns whether the calendar popup is enabled.
clear()	-  Clears or resets the editor.



# QDateTimeEdit Signals

Signal	-  Description
----------------------------------------------------------------------------------
dateChanged(QDate)	Emitted when the date changes.
timeChanged(QTime)	Emitted when the time changes.
dateTimeChanged(QDateTime)	Emitted when the date or time changes.
editingFinished()	Emitted when editing is completed.



# QDate Methods

Method	-  Description
----------------------------------------------------------------------------------
currentDate()	-  Returns the current system date.
day()	-  Returns the day of the month.
month()	-  Returns the month number.
year()	-  Returns the year.
dayOfWeek()	-  Returns the day of the week (1–7).
dayOfYear()	-  Returns the day number within the year.
daysInMonth()	-  Returns the number of days in the current month.
daysInYear()	-  Returns the number of days in the current year.
isValid()	-  Checks if the date is valid.
toString()	-  Converts the date to a formatted string.
addDays()	-  Returns a new date after adding days.
addMonths()	-  Returns a new date after adding months.
addYears()	-  Returns a new date after adding years.



# QTime Methods

Method	-  Description
----------------------------------------------------------------------------------
currentTime()	-  Returns the current system time.
hour()	-  Returns the hour.
minute()	-  Returns the minute.
second()	-  Returns the second.
msec()	-  Returns the milliseconds.
isValid()	-  Checks if the time is valid.
toString()	-  Converts the time to a formatted string.
addSecs()	-  Returns a new time after adding seconds.
addMSecs()	-  Returns a new time after adding milliseconds.

'''