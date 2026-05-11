# Import the car class from classes.py
from classes import Car

# Create a subclass of Car
class ElectricCar(Car):
    def __init__(self, brand=None, model=None, battery_capacity=None) -> None:
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def car_details(self):
        parent_details = super().car_details()  # get base details
        return f"{parent_details}, Battery: {self.battery_capacity} kWh"


my_electric = ElectricCar("Tesla", "Model S", 100)
old_car = Car("Toyota", "Corolla")

#print(my_electric.car_details())
#print(old_car.car_details())
