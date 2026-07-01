# Parent Class
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Car:", self.brand, self.model)


# Child Class
class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


#  object
car1 = ElectricCar("Tesla", "Model 3", "75 kWh")

car1.display()
print("Battery Size:", car1.battery_size)