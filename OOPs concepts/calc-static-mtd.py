# STATIC METHOD

class calc_static:
    
    @staticmethod
    def add(a,b):
        add = a + b
        print(f'Addition : {add}')

    @staticmethod
    def sub(a,b):
        sub = a - b
        print(f'Subtraction : {sub}')

    @staticmethod
    def mul(a,b):
        mul = a * b
        print(f'Multiplication : {mul}')

    @staticmethod
    def div(a,b):
        if b != 0:
            div = a / b
            print(f'Division : {div}')
        else:
            print('Division by zero error')
    
p1 = calc_static.add(10,20)

p2 = calc_static()
p2.sub(10,20)

p1 = calc_static.mul(10,20)

p2 = calc_static()
p2.div(10,100)