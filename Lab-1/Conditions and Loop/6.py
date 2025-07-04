positives = negatives = zeros = 0
for i in range(10):
    num = int(input(f"Enter integer {i+1}: "))
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1
    else:
        zeros += 1
print("Positive numbers:", positives)
print("Negative numbers:", negatives)
print("Zeros:", zeros)
