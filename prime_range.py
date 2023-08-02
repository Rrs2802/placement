def is_prime(number):
    if number % 2 == 0:
        return False
    else:
        for i in range(3, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        else:
            return True
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for number in range(start, end + 1):
    if is_prime(number):
        print(number)
