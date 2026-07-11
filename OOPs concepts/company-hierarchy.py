class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_person(self):
        print('Name : ',self.name)
        print('Age : ',self.age)

class employee(person):
    def __init__(self,name,age,empid,salary):
        super().__init__(name,age)
        self.empid = empid
        self.salary = salary

    def display_employee(self):
        self.display_person()
        print('EmpID : ',self.empid)
        print('Salary : ',self.salary)

class manager(employee):
    def __init__(self,name,age,empid,salary,dept):
        super().__init__(name,age,empid,salary)
        self.dept = dept

    def display_manager(self):
        self.display_employee()
        print('Department : ',self.dept)
    
m = manager('Jaidev',19,100,50000,'AI ML')
m.display_manager()

    