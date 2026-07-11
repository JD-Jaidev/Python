# HIERARCHICAL INHERITANCE

class vehicle:
    def __init__(self,brand):
        self.brand = brand

    def display_vehicle(self):
        print('Brand : ',self.brand)

class car(vehicle):
    def __init__(self,brand,seats):
        super().__init__(brand)
        self.seats = seats

    def display_car(self):
        self.display_vehicle()
        print('No. of seats : ',self.seats)

class bike(vehicle):
    def __init__(self,brand,mileage):
        super().__init__(brand)
        self.mileage = mileage

    def display_bike(self):
        self.display_vehicle()
        print('Mileage : ',self.mileage)

class bus(vehicle):
    def __init__(self,brand,capacity):
        super().__init__(brand)
        self.capacity = capacity

    def display_bus(self):
        self.display_vehicle()
        print('Capacity : ',self.capacity)


car = car('BMW',5)
bike = bike('Honda',)
bus = bus('Volvo',30)

print('Car details ---')
car.display_car()

print('Bike details ---')
bike.display_bike()

print('Bus details ---')
bus.display_bus()