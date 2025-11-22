def reverse_list(lst):
    return lst[::-1]
input_list = input("Enter elements separated by spaces: ")
numbers = list(map(int, input_list.split()))
print("Reversed list:", reverse_list(numbers))