# Write your code below this line
"""def prime_checker(number):
    checker = 0
    for div in range(1, number):
        if number % div == 0:
            checker += 1
    if checker > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")"""


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Your code above this line 👆
n = int(input("Please give a number to check\n"))  # Check this number
prime_checker(number=n)

