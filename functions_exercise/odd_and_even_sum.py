def odd_and_even(number):
    sum_even = 0
    sum_odd = 0
    for char in number:
        if int(char) % 2 == 0:
            sum_even += int(char)
        else:
            sum_odd += int(char)
    return sum_odd, sum_even


number_string = input()
sum_odd, sum_even = odd_and_even(number_string)
print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")
