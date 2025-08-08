def sum_numbers(*args):
    return sum(args)

nums = list(map(float, input("Enter numbers separated by space: ").split()))
print(sum_numbers(*nums))
