from abc import ABC,abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
class rectangle(shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
circle = circle(10)
rectangle = rectangle(10,20)

print(f'Area of circle : {circle.area():.2f}')
print(f'Area of rectangle : {rectangle.area():.2f}')