dict1 = {'a': 5, 'b': 3, 'c': 2}
dict2 = {'b': 4, 'c': 1, 'd': 7}

merged = dict1.copy()
for key, value in dict2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value

print("Merged dictionary:", merged)
