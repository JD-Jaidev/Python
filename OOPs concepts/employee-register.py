# SUPER KEYWORD AND INHERITANCE

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f'Your name is : {self.name}')
        print(f'Your age is : {self.age}')

class employee(person):
    def __init__(self, name, age, empid):
        super().__init__(name, age)
        self.empid = empid
    
    def display_employee(self):
        self.display_person()
        print(f'Your EmpID is : {self.empid}')

e1 = employee('Jai',10,100)
e2 = employee('Dev',20,200)
e3 = employee('Thanu',30,300)

lst = [e1,e2,e3]

for employee in lst:
    employee.display_employee()
    print('------------------------')


