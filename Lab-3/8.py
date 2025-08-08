nums = list(map(int, input("Enter numbers separated by space: ").split()))
div_by_10 = list(filter(lambda x: x % 10 == 0, nums))
print(div_by_10)
