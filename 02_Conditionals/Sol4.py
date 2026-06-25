fruit = input("Enter fruit name: ")
color = input("Enter fruit color: ")

if fruit.lower() == "banana":
    if color.lower() == "green":
        print("Unripe")
    elif color.lower() == "yellow":
        print("Ripe")
    elif color.lower() == "brown":
        print("Overripe")
    else:
        print("Invalid color")
else:
    print("Fruit data not available")