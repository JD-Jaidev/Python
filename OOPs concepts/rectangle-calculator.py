# CONSTRUCTOR AND INSTANCE METHODS

class rectangle_calc:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self,obj_name):
        area = self.length * self.breadth
        print(f'Area of rectangle {obj_name} = {area}cm²')
    def perimeter(self,obj_name):
        perimeter = 2 * (self.length + self.breadth)
        print(f'Perimeter of rectangle {obj_name} = {perimeter}cm')

r1 = rectangle_calc(10,20)
r1.area('r1')
r1.perimeter('r1')

r2 = rectangle_calc(30,40)
r2.area('r2')
r2.perimeter('r2')

r3 = rectangle_calc(50,60)
r3.area('r3')
r3.perimeter('r3')