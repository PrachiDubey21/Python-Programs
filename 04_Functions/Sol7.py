# *args allows a function to accept any number of arguments. 
# Inside the function, args is stored as a tuple.

#----------------------------------------------------------------------

# calculate the sum of numbers
def add(*args):

    # total = 0
    # for num in args:
    #     total += num
    # return total
    return sum(args)


result = add(10, 20, 30, 40, 50)
print("Sum =", result)

#----------------------------------------------------------------------------

# calculate the sum of numbers with user input
def add(*args):

    total = 0
    for num in args:
        total += num
    return total


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = add(*numbers)
print("Sum =", result)