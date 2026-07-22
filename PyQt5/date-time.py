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