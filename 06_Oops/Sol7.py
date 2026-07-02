# A static method is a method that belongs to the class, 
# not to any specific object.

# It is created using the @staticmethod decorator.

# Unlike normal methods:

# It does not use self because it does not access object data.
# It does not use cls because it does not access class data.
# It performs a general task related to the class.

# Create a class
class Car:

    # Static method
    @staticmethod
    def general_description():
        return "Cars are used for transportation."

# Call static method using the class name
print(Car.general_description())

#using object
car1 = Car()
print(car1.general_description())