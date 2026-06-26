while True:
    num = int(input("Enter a number between 1 and 10: "))

    if num >= 1 and num <= 10:
        print("Valid Input")
        break
    else:
        print("Invalid Input. Try Again.")