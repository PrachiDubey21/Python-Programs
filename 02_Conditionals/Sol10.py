species = input("Enter pet species: ")
age = int(input("Enter pet age: "))

if species.lower() == "dog":
    food = "Puppy Food" if age < 2 else "Adult Dog Food"

elif species.lower() == "cat":
    food = "Senior Cat Food" if age > 5 else "Regular Cat Food"

else:
    food = "No Recommendation Available"

print("Recommended Food:", food)