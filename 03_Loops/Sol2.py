n = int(input("Enter a number: "))
sum = 0
count = 0

# for i in range(n):
for i in range(1 , n+1):
    if i % 2 == 0:
        sum += i
        count+=1

print("Sum of even numbers:", sum)
print("Count of even numbers:", count)