for num in range(100, 1000):
    digits = [int(d) for d in str(num)]
    if sum(d ** 3 for d in digits) == num:
        print(num)
