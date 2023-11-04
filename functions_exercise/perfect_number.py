def aliquot_sum(num):
    aliquot_sum_number = 0
    divisor = 1
    for number in range(1, num // 2 + 1):
        if num % divisor == 0:
            aliquot_sum_number += divisor
        divisor += 1
    return aliquot_sum_number


number_input = int(input())
perfect_num = aliquot_sum(number_input)
if number_input == perfect_num:
    print("We have a perfect number!")

else:
    print("It's not so perfect.")
