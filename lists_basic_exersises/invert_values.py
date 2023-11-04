list_numbers = input().split(" ")
opposite_numbers = []

for element in list_numbers:
    current_element = -int(element)
    opposite_numbers.append(current_element)
print(opposite_numbers)
