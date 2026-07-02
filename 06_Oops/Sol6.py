# A class variable is a variable that belongs to the class itself,
# not to individual objects.

# It is shared by all objects of the class.
# If its value changes, the updated value is seen by every object.
# It is declared outside all methods but inside the class

#-------------------------------------------------------------------------

class Car:

    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        Car.total_cars += 1

car1 = Car("Toyota", "Fortuner")
car2 = Car("Honda", "City")
car3 = Car("Tesla", "Model Y")

print("Total Cars:", Car.total_cars)