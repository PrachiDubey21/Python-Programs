num = int(input("Enter a number: "))
isPrime = True

if num <= 1:
    isPrime = False
else:
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

if isPrime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")