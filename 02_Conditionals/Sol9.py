# A year is a leap year if it is divisible by 4.
# But if it is divisible by 100, it is not a leap year.
# However, if it is also divisible by 400, then it is a leap year.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")