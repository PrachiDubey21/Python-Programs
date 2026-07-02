# Class
class Car:

    # Constructor
    def __init__(self, brand, model):
        self.__brand = brand             # Private attribute
        self.model = model

    # Getter method
    def get_brand(self):
        return self.__brand

# Object
car1 = Car("Toyota", "Fortuner")


# accessing private attribute using getter
print("Brand:", car1.get_brand())

# accessing public attribute
print("Model:", car1.model)