distance = float(input("Enter distance in km: "))

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("Recommended Transportation:", transport)