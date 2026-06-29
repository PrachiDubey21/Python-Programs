# **kwargs allows a function to accept any number of keyword arguments.
# Inside the function, kwargs is stored as a dictionary.

#-------------------------------------------------------------------------

#  print keyword arguments
def details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


#call the function
details( name="Prachi", age=20, city="Bhopal", course="B.Tech")