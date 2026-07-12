# DECORATORS IN PYTHON

def add_sprinkles(func):
    def wrapper(flavor):
        print('Adding sprinkles !')
        func(flavor)
        print('Your total bill is :50')
    return wrapper

@add_sprinkles
def get_icecream(flavor):
    print(f'You have chosen {flavor} Ice cream.')

get_icecream('Chocolate')