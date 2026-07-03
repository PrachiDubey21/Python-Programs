# Decorator function
def cache(func):

    # Dictionary to store cached results
    memory = {}

    # Wrapper function
    def wrapper(*args):

        # if result is already stored
        if args in memory:
            print("Returning Cached Value")
            return memory[args]

        # Else execute the function
        result = func(*args)

        # Store result in dictionary
        memory[args] = result

        return result

    return wrapper


@cache
def square(num):
    print("Calculating Square...")
    return num * num


print(square(5))
print(square(5))
print(square(10))
print(square(10))

#------------------------------------------------------------------

# square(5)
#       │
#       ▼
# wrapper(5)
#       │
#       ▼
# Is (5,) in memory?
#       │
#       ├── No
#       │      │
#       │      ▼
#       │ Execute square()
#       │      │
#       │      ▼
#       │ Store Result
#       │
#       ▼
# Return 25

# Second Call

# square(5)
#       │
#       ▼
# wrapper(5)
#       │
#       ▼
# Is (5,) in memory?
#       │
#       ├── Yes
#       │      │
#       │      ▼
#       │ Return Cached Value
#       ▼
# Return 25