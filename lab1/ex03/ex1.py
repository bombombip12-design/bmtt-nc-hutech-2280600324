def total_even_numbers(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total
input_listnumbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_listnumbers.split()))
result = total_even_numbers(numbers)
print("The total of even numbers is:", result)