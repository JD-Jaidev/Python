class engine:
    def __init__(self,horse_power):
        self.horse_power = horse_power

class wheel:
    def __init__(self,wheel_size):
        self.wheel_size = wheel_size

class car:
    def __init__(self,make,model,horse_power,wheel_size,):
        self.make = make
        self.model = model
        self.engine = engine(horse_power)
        self.wheel = wheel(wheel_size)

    def display_car(self):
        return f'{self.make} : {self.model} : {self.engine.horse_power} : {self.wheel.wheel_size}'
    
c = car('BMW','M4',500,20)
print(c.display_car())