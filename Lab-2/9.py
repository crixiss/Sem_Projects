import random

numbers = set()
while len(numbers) < 10:
    numbers.add(random.randint(1, 20))

print("Original set:", numbers)
numbers.remove(min(numbers))
numbers.remove(max(numbers))
print("After removing min and max:", numbers)
