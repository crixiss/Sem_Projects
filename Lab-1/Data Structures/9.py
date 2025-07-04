list1_input = input("Enter elements of first list separated by spaces: ")
list2_input = input("Enter elements of second list separated by spaces: ")

list1 = list1_input.split()
list2 = list2_input.split()

result = [item for item in list1 if item not in list2]

print("Resulting list:", result)
