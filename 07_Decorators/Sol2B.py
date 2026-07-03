
# Debug Decorator
def debug(func):

    # Wrapper function accepts any number of positional
    # and keyword arguments
    def wrapper(*args, **kwargs):

        # Convert positional arguments into a string
        args_value = ', '.join(str(arg) for arg in args)

        # Convert keyword arguments into a string
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())

        # Print function name and arguments
        print(f"Calling: {func.__name__} with args ({args_value}) and kwargs ({kwargs_value})")

        # Call the original function
        return func(*args, **kwargs)

    return wrapper


# Decorator applied
@debug
def hello():
    print("Hello")


# Decorator applied
@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


# Decorator applied
@debug
def add(a, b):
    print("Sum =", a + b)


# Function calls
hello()
print()
greet("Chai", greeting="Hanji")
print()
add(10, 20)

#-------------------------------------------------------------------------

# *args collects all positional arguments into a tuple.

# **kwargs collects all keyword arguments into a dictionary.

# args_value converts the tuple into a readable string like "1, 2, 3".

# kwargs_value converts the dictionary into a readable 
# string like "name=Alice, age=20".

# func.__name__ gives the name of the decorated function.

# func(*args, **kwargs) calls the original function with exactly 
# the same arguments it received. This is what allows the
# decorator to work with almost any function.
