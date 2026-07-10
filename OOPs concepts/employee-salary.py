class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def increment(self):
        self.salary = self.salary + self.salary * 0.1
        print(f'New salary : {self.salary}')
        
e1 = employee('Jai',10000)
e1.increment()

e2 = employee('Dev',20000)
e2.increment()