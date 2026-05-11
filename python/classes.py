class Car:
    # Class variables
    total_car = 0

    def __init__(self, brand=None, model=None) -> None:
        # Private access through functions
        self.__brand = brand
        self.__model = model
        self.total_car += 1
        # Public direct access
        # self.brand = brand
        # self.model = model

    # Getter for brand
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    # Setter for model
    def set_model(self, model):
        self.__model = model

    def car_details(self):
        return f"Car Name: {self.__brand}, Car Model: {self.__model}"  # within the class access is allowed but not outside

    def start_engine(self):
        return f"{self.get_brand()} is powering up silently (electric engine)..."

    # Static method decorator
    @staticmethod
    def general_discription():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model


my_car = Car("Toyota", "Corolla")
new_car = Car()
# check if class is a instance of class car
#print(isinstance(my_car, Car))
#print(my_car.car_details())
#print(Car.general_discription())
