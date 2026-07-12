# PRIVATE VARIABLES, ENCAPSULATION AND GETTER SETTER METHODS

class bank_account:
    def __init__(self,name,balance):
        self.name = name 
        self.__balance = balance   # private variable 
        print(f'\n Welcome {self.name}')
        

    def deposit(self,amount):
        if amount < 0:
            print('Invalid deposit amount')
        else:
            self.__balance += amount
            print(f'{amount} deposited successfully !')

    def withdraw(self,amount):
        if amount > self.__balance:
            print('Not enough balance')
        elif amount < 0:
            print('Invalid withdraw amount') 
        else:
            self.__balance -= amount
            print(f'{amount} withdrawn successfully !')

    def get_balance(self):
        return f'Current balance : {self.__balance}' 
    
c = bank_account('Jaidev',10000)
c.deposit(5000)
c.withdraw(10000)

print(c.get_balance())

d = bank_account('Thanish',10000)
d.deposit(7000)
d.withdraw(8000)

print(d.get_balance())