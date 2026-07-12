class person:
    def  __init__(self,name,age):
        self._name = name
        self.age = age

class employee(person):
    def __init__(self, name, age, empid):
        super().__init__(name, age)
        self.empid = empid

    def display_employee(self):
        print(f'\n Welcome : {self._name}')
        print(f'Age : {self.age}')
        print(f'EmpID : {self.empid}')

e1 = employee('Jai',10,100)
e2 = employee('Dev',20,200)
e3 = employee('Thanish',30,300)

lst = [e1,e2,e3]
for employee in lst:
    employee.display_employee()

