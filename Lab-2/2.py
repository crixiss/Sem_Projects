a = list(map(int, input("Enter list A: ").split()))
b = list(map(int, input("Enter list B: ").split()))
merged = a + b
unique = [x for x in merged if not (x in a and x in b)]
print("Merged without common:", unique)
