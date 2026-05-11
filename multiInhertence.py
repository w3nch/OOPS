from classes import Car
from inheritance import ElectricCar


class Battery:
    def batter_info(self):
        return "Battery good"


class Engine:
    def enginer_info(self):
        return "engine good"


class SportsCar(ElectricCar, Battery, Engine):
    pass


my_new_sportscar = SportsCar("Lambo", "Huracan", 90)  # 90 kWh battery
print(my_new_sportscar.car_details())  # from ElectricCar -> Car
print(my_new_sportscar.batter_info())  # from Battery
print(my_new_sportscar.enginer_info())  # from Engine
print(my_new_sportscar.start_engine())  # ElectricCar method
