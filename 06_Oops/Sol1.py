
class Car:

    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Object
car1 = Car("Toyota", "Fortuner")

print("Brand:", car1.brand)
print("Model:", car1.model)