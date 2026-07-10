class BankAccount:
    def __init__(self,acc_number,acc_name,balance):
        self.acc_number = acc_number
        self.acc_name = acc_name
        self.__balance = balance

    def deposit(self,deposit):
        if deposit > 0: 
            self.__balance += deposit
            print(f'Amount deposited : {deposit}')
        else:
            print('Invallid deposit amount')

    def withdraw(self,withdraw):
        if withdraw <= 0:
            print('Invalid withdraw amount')
        elif withdraw > self.__balance:
            print('insufficient balance')
        else:
            self.__balance -= withdraw
            print(f'Amount withdrawn : {withdraw}')

    def display(self):
        print('\n Account Details')
        print('--------------------------------------')
        print(f'Account number : {self.acc_number}')
        print(f'Account holder : {self.acc_name}')
        print(f'Balance : {self.__balance}')
    
p1 = BankAccount(100,'JAI',10000)

dep = int(input('Enter the amount you want to deposit : '))
p1.deposit(dep)
p1.display()

withd = float(input('Enter the amount you want to withdraw : '))
p1.withdraw(withd)
p1.display()