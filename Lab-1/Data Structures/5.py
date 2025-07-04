prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}

num = int(input("Enter a number: "))
if num in prime_numbers:
    print(num, "is a prime number less than 50.")
else:
    print(num, "is not in the set of primes less than 50.")
