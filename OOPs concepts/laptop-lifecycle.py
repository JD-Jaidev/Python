# USING __del__()

class laptop:
    # constructor
    def __init__(self,brand):
        self.brand = brand
        print(f'The laptop is : {self.brand}')
    
    # destructor
    def __del__(self):
        print(f'The laptop {self.brand} is shut down...')

lap = laptop('Lenovo')

