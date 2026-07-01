
# Class
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Car Name:", self.brand, self.model)

# input from the user
brand = input("Enter car brand: ")
model = input("Enter car model: ")

# Create object
car = Car(brand, model)

# Display details
car.display()