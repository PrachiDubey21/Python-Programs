size = input("Enter coffee size (Small/Medium/Large): ")
extra_shot = input("Do you want an extra shot? (Yes/No): ")

if extra_shot.lower() == "yes":
    print(size, "Coffee with Extra Shot")
else:
    print(size, "Coffee")