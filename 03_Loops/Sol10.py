wait_time = int(input("Enter Initial Wait Time: "))
tries = 1

while tries <= 5:

    print("Retry", tries, "- Wait", wait_time, "second(s)")
    wait_time *= 2
    tries += 1