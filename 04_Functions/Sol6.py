# A lambda function is a small, anonymous (nameless) function 
# that can take any number of arguments but contains only one expression

# lambda arguments: expression

#------------------------------------------------------------------------

# Lambda function to calculate cube
cube = lambda num: num ** 3

number = int(input("Enter a number: "))
result = cube(number)

print("Cube =", result)