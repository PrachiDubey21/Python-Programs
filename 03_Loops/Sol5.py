# The else here belongs to the for loop, not the if statement.
# The else block executes only if the loop finishes normally,
# without encountering a break.

text = input("Enter a string: ")

for char in text:

    # in built function
    if text.count(char) == 1:
        print("First non-repeated character:", char)
        break
else:
    print("No non-repeated character found")