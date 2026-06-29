# In Python, the same * operator behaves differently depending on the data type:

# For numbers, it performs multiplication.
# For strings, it repeats the string.

#------------------------------------------------------------------------------

# Function to multiply two numbers
def multiply(a, b):
    return a * b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = multiply(num1, num2)
print("Result =", result)

#-----------------------------------------------------------------------------

# Function to multiply a string
def multiply(text, times):
    return text * times

text = input("Enter a string: ")
times = int(input("Enter how many times to repeat: "))

result = multiply(text, times)
print("Result =", result)

#---------------------------------------------------------------------------

# Function to multiply values
def multiply(a, b):
    return a * b

print(multiply(5, 4))
print(multiply("Hi", 3))