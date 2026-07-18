# BANKING PROGRAM


def view_balance(balance):
    print(f'Your balance is : ₹{balance}')

def deposit(balance):
    deposit = float(input('Enter the amount you want to deposit : ₹'))
    balance += deposit
    print(f'Amount to be deposited : ₹{deposit}')
    print(f'Your new balance is : ₹{balance}')
    return balance

def withdraw(balance):
    withdraw = float(input('Enter the amount you want to withdraw : ₹'))
    balance -= withdraw
    print(f'Amount to be withdrawn : ₹{withdraw}')
    print(f'Your new balance is : ₹{balance}')
    return balance

def main():
    print('Welcome to Banking program !')
    print('----------------------------')
    print('1. Check balance')
    print('2. Deposit amount')
    print('3. Withdraw amount')
    print('4. Exit')
    print('----------------------------')

    balance = 10000
    opt = 'y'
    while opt.lower() == 'y':
        choice=int(input('Enter choice to perform operation : '))

        if choice == 1:
            view_balance(balance)
        elif choice == 2:
            balance = deposit(balance)
        elif choice == 3:
            balance = withdraw(balance)
        elif choice == 4:
            break
        else:
            print('Invalid choice. Enter a valid choice.')
        opt = input('Do you want to perform another operation ? (y/n) : ')
    print(f'Thank you for using Python Banking program. Your final balance is ₹{balance}')

if __name__ == '__main__':
    main()
    
