num = int(input("Enter a number: "))
nums = num
fact = 1

while num > 0:
    fact *= num
    num -= 1

print("Factorial of", nums, "is", fact)