
def abs_numbers():
    list_numbers = input().split()
    list_numbers_int = []
    for num in list_numbers:
        current_num = abs(float(num))
        list_numbers_int.append(current_num)

    print(list_numbers_int)


abs_numbers()
