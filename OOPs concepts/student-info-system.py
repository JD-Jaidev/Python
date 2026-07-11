# CLASSES, OBJECTS, INSTANCE VARIABLES AND CONSTRUCTORS

class student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def show(self):
        print(f'Student name : {self.name}')
        print(f'Student roll no. : {self.roll}')
        print(f'Student marks : {self.marks}')

s1 = student('Jai',1,90)
s1.show()

s2 = student('Dev',2,80)
s2.show()