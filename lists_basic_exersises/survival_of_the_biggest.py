list_numbers = input().split()
count_numbers_to_remove = int(input())
list_numbers_digits = []

for element in list_numbers:
    list_numbers_digits.append(int(element))
for number in range(count_numbers_to_remove):
    list_numbers_digits.remove(min(list_numbers_digits))

print(', '.join(map(str, list_numbers_digits)))

