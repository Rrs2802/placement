num = int(input("Enter a number: "))
num_str = str(num)
rev_str = num_str[::-1]
if num_str == rev_str:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
