# CAR RENTAL SYSTEM USING ABSTRACT CLASSES

from abc import ABC,abstractmethod

# ABSTRACT CLASS

class vehicle(ABC):
    def __init__(self,vehicle_no,brand,price_per_day):
        self.vehicle_no = vehicle_no
        self.brand = brand
        self.price_per_day = price_per_day

    @abstractmethod
    def calculate_rent(self,days):
            pass
        
    def display(self):
        print(f'\n Vehicle Number : {self.vehicle_no}')
        print(f'Brand : {self.brand}')
        print(f'Price/Day : {self.price_per_day}')

# CAR CLASS

class car(vehicle):
    def calculate_rent(self,days):
        return self.price_per_day * days
    
# BIKE CLASS 

class bike(vehicle):
    def calculate_rent(self,days):
        rent = self.price_per_day * days
        if days > 7:
            rent -= rent * 0.05

        return rent 
    
# TRUCK CLASS

class truck(vehicle):
    def calculate_rent(self,days):
        return (self.price_per_day * days) + (500 * days)
    
# MAIN PROGRAM

total_bill = 0
vehicles = []

while True:
    print('\n ----------- Vehicle Rental System -----------')
    print('1. Car')
    print('2. Bike')
    print('3. Truck')
    print('4. Exit')

    choice = int(input('Enter choice : '))

    if choice == 4:
        break
    
    vehicle_no = input("Enter Vehicle Number: ")
    brand = input("Enter Brand: ")
    price = float(input("Enter Rental Price per Day: "))
    days = int(input("Enter Number of Rental Days: "))

    if choice == 1:
        vehicle = car(vehicle_no, brand, price)

    elif choice == 2:
        vehicle = bike(vehicle_no, brand, price)

    elif choice == 3:
        vehicle = truck(vehicle_no, brand, price)

    else:
        print("Invalid Choice!")
        continue

    rent = vehicle.calculate_rent(days)

    vehicles.append((vehicle, days, rent))
    total_bill += rent

    print(f"\nRent for this vehicle: ₹{rent:.2f}")

# Final Bill
print("\n---------------- Rental Summary ----------------")

for vehicle, days, rent in vehicles:
    vehicle.display()
    print(f"Rental Days    : {days}")
    print(f"Rent           : ₹{rent:.2f}")

print("\n------------------------------------------------")
print(f"Total Vehicles Rented : {len(vehicles)}")
print(f"Total Bill            : ₹{total_bill:.2f}")