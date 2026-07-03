# A decorator is a function that adds extra functionality 
# to another function without changing its original code.


import time

# Decorator function
def timer(func):

    # Wrapper function
    def wrapper():

        # Record start time
        start = time.time()

        # Call the original function
        func()

        # Record end time
        end = time.time()

        # Calculate execution time
        print("Execution Time:", end - start, "seconds")

    return wrapper


# Apply decorator
@timer
def display():

    # Delay for 2 seconds
    time.sleep(2)
    print("Function is running...")


# Call the function
display()


#--------------------------------------------------------------------------

# @timer
# def display():

# it automatically converts it to
# display = timer(display)

# So instead of calling the original display() directly,
# display()
# It actually calls
# wrapper()

# display()
#      │
#      ▼
# wrapper()
#      │
#      ▼
# Record Start Time
#      │
#      ▼
# Run display()
#      │
#      ▼
# time.sleep(2)
#      │
#      ▼
# Print "Function is running..."
#      │
#      ▼
# Record End Time
#      │
#      ▼
# Calculate end - start
#      │
#      ▼
# Print Execution Time