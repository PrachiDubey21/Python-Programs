items = ["apple", "banana", "orange", "litchi", "mango"]
basket = []

for item in items:

# if item is already present it is duplicate
    if item in basket:
        print("Duplicate Found:", item)
        break

# else add it in basket
    basket.append(item)

else:
    print("All elements are unique.")