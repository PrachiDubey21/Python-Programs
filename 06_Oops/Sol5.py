
# Parent Class
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Parent class method
    def fuel_type(self):
        return "Petrol or Diesel"


# Child Class
class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    # Overriding the parent class method
    def fuel_type(self):
        return "Electric Charge"


car1 = Car("Toyota", "Fortuner")
car2 = ElectricCar("Tesla", "Model 3", "75 kWh")

print(car1.fuel_type())
print(car2.fuel_type())