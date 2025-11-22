def create_tuple_from_list(input_list):
    return tuple(input_list)
input_list = input("Enter elements separated by spaces: ")
numbers = list(map(int, input_list.split()))
my_tuple = create_tuple_from_list(numbers)
print("Created tuple:", my_tuple)
print("List: ", numbers)