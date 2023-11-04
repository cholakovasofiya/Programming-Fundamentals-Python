factor = int(input())
count_numbers = int(input())
length_list = factor * count_numbers

list_numbers = []
for number in range(factor, length_list + 1, factor):
    list_numbers.append(number)
print(list_numbers)
