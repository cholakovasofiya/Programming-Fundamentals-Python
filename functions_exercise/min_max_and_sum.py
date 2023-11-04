def str_to_int(list_input):
    lst_numbers = []
    for element in list_input:
        lst_numbers.append(int(element))
    return lst_numbers


sequence_numbers = input().split()
converted_numbers = str_to_int(sequence_numbers)
min_number = min(converted_numbers)
max_number = max(converted_numbers)
sum_numbers = sum(converted_numbers)
print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")
