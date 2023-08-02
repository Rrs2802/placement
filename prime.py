number=int(input("enter a number:"))
if number % 2 == 0:
    print("The number is not prime.")
else:
    for i in range(3, int(number ** 0.5) + 1):
        if number % i == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is prime.")
