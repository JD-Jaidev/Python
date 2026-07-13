class complex_number:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return complex_number(real,imaginary)
    
    def __str__(self):
        return f'{self.real} + {self.imaginary}i'
    
c1 = complex_number(2,3)
c2 = complex_number(4,5)

result = c1 + c2

print(f'First complex number : {c1}')
print(f'Second complex number : {c2}')

print(f'Sum : {result}')