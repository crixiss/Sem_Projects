names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice']

name_counts = {}
for name in names:
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1

print("Name counts:", name_counts)
