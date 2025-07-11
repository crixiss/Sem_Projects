n=int(input("Enter a number: "))
lst = []

for _ in range(n):
    lst.append(int(input("Enter number: ")))

print("Maximum is:", max(lst))
print("Minimum is:", min(lst))
print("Sorted list is:", sorted(lst))
print("Removed duplicates are:", list(set(lst)))
