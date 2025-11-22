def Count_number_occurences(input_list):
    count_dict = {}
    for item in input_list:
        if item in count_dict:
            count_dict[item] = + 1
        else:
            count_dict[item] = 1
    return count_dict
input_string = input("Enter elements separated by spaces: ")
word_list = input_string.split()
result = Count_number_occurences(word_list)
print("Element occurrences:", result)