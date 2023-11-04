count_number = int(input())
delimiter = "->"

for num in range(1, count_number + 1):
    sum_of_digits = 0
    digits = num
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)

    if sum_of_digits == 5 or sum_of_digits == 7 \
            or sum_of_digits == 11:
        special_number = True
        print(f"{num} {delimiter} {special_number}")
    else:
        special_number = False
        print(f"{num} {delimiter} {special_number}")
