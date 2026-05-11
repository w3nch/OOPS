# polymorphism.py
from classes import Car


# Subclass for sports cars
class SportsCar(Car):
    def start_engine(self):
        return f"{self.get_brand()} roars to life with a V8 engine!"


# Subclass for hybrid cars
class HybridCar(Car):
    def __init__(
        self, brand=None, model=None, fuel_capacity=None, battery_capacity=None
    ) -> None:
        super().__init__(brand, model)
        self.__fuel_capacity = fuel_capacity
        self.__battery_capacity = battery_capacity

    def car_details(self):
        return f"{super().car_details()}, Fuel: {self.__fuel_capacity} L, Battery: {self.__battery_capacity} kWh"

    def start_engine(self):
        return f"{self.get_brand()} starts with a combination of fuel and electric power..."


# Polymorphism demo
def main():
    vehicles = [
        SportsCar("Ferrari", "F8"),
        HybridCar("Toyota", "Prius", 40, 10),
    ]

    for v in vehicles:
        print(v.car_details())
        print(v.start_engine())
        print("-" * 50)


if __name__ == "__main__":
    main()
