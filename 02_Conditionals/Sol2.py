
age = int(input("Enter your age: "))
day = input("Enter the day: ")

if age >= 18:
    price = 12
else:
    price = 8

if day == "Wednesday":
    price = price - 2

print("Ticket price: $", price)