# SLOT MACHINE

import random

def spin_row():
    symbols = ['🥪' , '🍭' , '🍟' , '🍔' , '🍕']
    for i in range(0,3):
        return [random.choice(symbols) for _ in range(3)]
    
def print_row(row):
    print('------------')
    print(' | '.join(row))
    print('------------')

def get_payout(row , bet):
    if row[0] == row[1] == row[2]:
        return bet*10
    return 0

def main():
    balance = 100
    while balance > 0:
        
        print('\n Welcome to python slots !')
        print('-------------------------')
        print('Symbols : 🥪 , 🍭 , 🍟 , 🍔 , 🍕')
        bet = float(input('Enter you bet amount : ₹'))
    
        if not bet:
            bet = float(input('Enter a valid number : '))
            continue

        if bet < 0:
            bet = float(input('Enter a positive number : '))
            continue

        if bet > balance:
            print('Insufficient balance')
            continue

        balance -= bet

        row = spin_row()
        print('\n Spinning...')
        print_row(row)

        payout = get_payout(row , bet)

        if payout > 0:
            print(f'You have won : ₹{payout}')
        else:
            print('Sorry you have lost this round')

        balance += payout
        print(f'Balance : ₹{balance}')

        play_again = input('Do you want to spin again (y/n) : ')
        if play_again.lower() == 'y':
            continue
        else:
            play_again.lower() != 'y'
            print('---------------------------------------------------------------------------')                                    
            print(f'Thank you for using Python slot machine. Your final balance is ₹{balance}.')
            print('---------------------------------------------------------------------------')
            break    

if __name__ == '__main__':
    main()
