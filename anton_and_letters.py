def trim_input_first_and_end(input_string):
    return input_string[1:len(input_string) - 1]


def remove_spaces_from_a_string(input_string):
    return input_string.replace(" ", "")


def unique(list1):
    unique_list = []

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)

    return unique_list


a_set_values = input()
a_set_without_braces = trim_input_first_and_end(a_set_values)
if a_set_without_braces == "":
    print("0")
else:
    a_set_string_reformated = remove_spaces_from_a_string(trim_input_first_and_end(a_set_values))
    set_array_values = a_set_string_reformated.split(",")
    unique_set = unique(set_array_values)
    print(len(unique_set))
