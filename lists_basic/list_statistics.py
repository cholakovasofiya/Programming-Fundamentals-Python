count_numbers = int(input())
positive_numbers = []
negative_numbers = []

for num in range(count_numbers):
    current_number = int(input())
    if current_number < 0:
        negative_numbers.append(current_number)
    else:
        positive_numbers.append(current_number)
print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")
