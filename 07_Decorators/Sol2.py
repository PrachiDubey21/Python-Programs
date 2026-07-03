# Decorator function
def debug(func):

    # Wrapper function
    def wrapper(*args):

        print("Function Name:", func.__name__)
        print("Arguments:", args)

        func(*args)

    return wrapper


@debug
def add(a, b):
    print("Sum:", a + b)


add(10, 20)


#-----------------------------------------------------------------------------

# add(10, 20)
#         │
#         ▼
# wrapper(10, 20)
#         │
#         ▼
# Print Function Name
#         │
#         ▼
# Print Arguments
#         │
#         ▼
# Call Original Function
# add(10, 20)
#         │
#         ▼
# Print Sum