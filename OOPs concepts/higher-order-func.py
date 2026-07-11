# HIGER ORDER FUNCTIONS

# 1. PASSING FUNCTIONS AS ARGUMENTS

# Eg - 1
def greet():
    print('hello')
def execute(func):
    func()

execute(greet)

# Eg - 2

def square(x):
    return x**2
def cube(x):
    return x**3

def perform(operation,number):
    return operation(number)

print(perform(square,4))
print(perform(cube,4))


# 2. RETURNING FUNCTIONS

# Eg - 1
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

div = divisor(2)
print(div(10))

# Eg - 2
def operation():
    def greet():
        print('hello world')
    return greet

x = operation()
x()
