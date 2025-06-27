
import random

numbers = []
for i in range(15):
    numbers.append(random.randint(1, 100))

print("All 15 numbers:", numbers)

random.shuffle(numbers)

group1 = numbers[0:5]
group2 = numbers[5:10]
group3 = numbers[10:15]

print("\nGroup 1:", group1)
print("Group 2:", group2)
print("Group 3:", group3)

sum1 = sum(group1)
sum2 = sum(group2)
sum3 = sum(group3)

print("\nSum of Group 1:", sum1)
print("Sum of Group 2:", sum2)
print("Sum of Group 3:", sum3)

if sum1 > sum2 and sum1 > sum3:
    print("\nGroup 1 wins!")
elif sum2 > sum1 and sum2 > sum3:
    print("\nGroup 2 wins!")
elif sum3 > sum1 and sum3 > sum2:
    print("\nGroup 3 wins!")
else:
    print("\nIt's a tie!")
