def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def filter_list(lst):
    return [x for i, x in enumerate(lst) if i % 2 == 0 or is_prime(x)]

lst = [2, 3, 4, 5, 6, 7, 8, 9]
print(filter_list(lst))
