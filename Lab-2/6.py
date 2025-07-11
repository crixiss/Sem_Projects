def calculate_stats(numbers):
    n = len(numbers)
    avg = sum(numbers) / n

    sorted_nums = sorted(numbers)
    median = sorted_nums[n//2] if n % 2 != 0 else (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2

    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    mode = max(freq, key=freq.get)

    return avg, median, mode

nums = (4, 1, 2, 2, 3, 5)
print(calculate_stats(nums))
