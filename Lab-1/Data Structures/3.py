numbers_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in numbers_input.split()]

def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

result = get_even_numbers(numbers)
print("Even numbers:", result)
