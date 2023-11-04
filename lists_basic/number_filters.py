count_numbers = int(input())
all_numbers = []

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_POSITIVE = "positive"
COMMAND_NEGATIVE = "negative"

for num in range(count_numbers):
    current_number = int(input())
    all_numbers.append(current_number)
command = input()

filtered_numbers = []
for number in all_numbers:
    filter_condition = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_POSITIVE and number >= 0) or
        (command == COMMAND_NEGATIVE and number < 0)
    )
    if filter_condition:
        filtered_numbers.append(number)
print(filtered_numbers)
