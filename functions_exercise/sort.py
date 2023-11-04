def number_converter(list_input):
    string_to_numbers = []
    for element in list_input:
        string_to_numbers.append(int(element))
    return string_to_numbers


lst = input().split()
list_numbers = number_converter(lst)
number_asc = sorted(list_numbers)
print(number_asc)
