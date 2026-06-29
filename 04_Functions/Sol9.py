# A generator function is a function that uses the
# yield keyword instead of return.

# return ends the function and sends back one value.
# yield pauses the function, returns one value, and remembers its state. 
# The next time the function is called, it continues from where it stopped.

# Generators are useful when working with large amounts of data 
# because they generate values one at a time instead of storing 
# all of them in memory.

#-------------------------------------------------------------------------

# range(start, stop, step)
# start → The number from where the loop starts.
# stop → The number where the loop stops (not included).
# step → How much to increase after each iteration.

#--------------------------------------------------------------------------

# Generator function
def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i


limit = int(input("Enter the limit: "))
result = even_numbers(limit)

for num in result:
    print(num)