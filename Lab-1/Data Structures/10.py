data = {}

n = int(input("How many key-value pairs? "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

search_key = input("Enter key to search: ")
if search_key in data:
    print("Value:", data[search_key])
else:
    print("Key not found.")
