def delete_element(dict, key):
    if key in dict:
        del dict[key]
        return True
    else:
        return False
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_delete = 'b'
result = delete_element(my_dict, key_to_delete)
if result:
    print("Element deleted successfully.", my_dict)
else:
    print("Key not found in dictionary.", my_dict)