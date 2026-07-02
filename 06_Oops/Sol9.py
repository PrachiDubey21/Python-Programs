# isinstance() is a built-in Python function used 
# to check whether an object belongs to a particular class.

# Syntax -:
# isinstance(object, ClassName)

#-----------------------------------------------------------------------

# Parent Class
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# Child Class
class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model 3", "75 kWh")

print(isinstance(my_tesla, ElectricCar))
print(isinstance(my_tesla, Car))



# my_tesla = Car("Tesla", "Model 3")
# print(isinstance(my_tesla, ElectricCar))
# print(isinstance(my_tesla, Car))