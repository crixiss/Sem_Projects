n=int(input("Enter the number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter number: ")))
max_val = lst[0]
min_val = lst[0]
for num in lst:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
sorted_lst = lst[:]
for i in range(n):
    for j in range(i+1, n):
        if sorted_lst[i] > sorted_lst[j]:
            sorted_lst[i], sorted_lst[j] = sorted_lst[j], sorted_lst[i]
no_duplicates = []
for num in lst:
    if num not in no_duplicates:
        no_duplicates.append(num)
print("Manual Max:", max_val)
print("Manual Min:", min_val)
print("Manual Sorted:", sorted_lst)
print("Duplicates:", no_duplicates)