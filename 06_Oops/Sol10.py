# Parent Class 1
class Battery:

    def battery_info(self):
        return "Battery Capacity: 75 kWh"


# Parent Class 2
class Engine:

    def engine_info(self):
        return "Electric Engine"


# Child Class
class ElectricCar(Battery, Engine):

    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = ElectricCar("Tesla", "Model 3")

print("Brand:", car1.brand)
print("Model:", car1.model)

print(car1.battery_info())
print(car1.engine_info())