n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

count = 0

for num in numbers:
    if num > 0:
        print(num)
        count += 1

print("Total Positive Numbers:", count)