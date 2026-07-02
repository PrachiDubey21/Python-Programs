# property decorator (@property) is used to make 
# a method behave like an attribute.

# Normally, methods are called using parentheses ().

# Example:
# print(car.get_model())

# With @property, the method can be accessed like a variable:
# print(car.model)

# It is useful in encapsulation for accesing pvt members

#--------------------------------------------------------------------------

# Create a class
class Car:

    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model     # Private attribute

    # Property decorator
    @property
    def model(self):
        return self.__model


# Create object
car1 = Car("Toyota", "Fortuner")

# Access model like an attribute
print("Brand:", car1.brand)
print("Model:", car1.model)