number = int(input("Enter a number: "))
isPrime = True

if number <= 1:
    isPrime = False
else:
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break

if isPrime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")