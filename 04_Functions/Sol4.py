
# calculate area and circumference
def circle(radius):

    pi = 3.14
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference


radius = float(input("Enter the radius: "))
area, circumference = circle(radius)

print("Area =", area)
print("Circumference =", circumference)