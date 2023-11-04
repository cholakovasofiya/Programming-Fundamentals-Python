number_of_chars = int(input())
sum_of_chars = 0

for num in range(number_of_chars):
    letter = input()
    sum_of_chars += ord(letter)
print(f"The sum equals: {sum_of_chars}")