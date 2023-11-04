def string_to_integer(list_input):
    list_converted_numbers = []
    for element in list_input:
        list_converted_numbers.append(int(element))
    return list_converted_numbers


def even_numbers(num):
    if num % 2 == 0:
        return True
    else:
        return False


sequence_numbers = input().split()
lst_numbers = string_to_integer(sequence_numbers)
result = filter(even_numbers, lst_numbers)
print(list(result))
