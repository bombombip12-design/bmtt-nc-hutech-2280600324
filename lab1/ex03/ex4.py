def element_access(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
input_tuple = eval(input("Enter tuple: "))
first, last = element_access(input_tuple)
print("First element:", first)
print("Last element:", last)