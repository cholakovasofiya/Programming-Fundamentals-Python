number_of_chars = int(input())

for first_char in range(number_of_chars):
    for second_char in range(number_of_chars):
        for third_char in range(number_of_chars):
            print(f"{chr(first_char+97)}{chr(second_char+97)}"
                  f"{chr(third_char+97)}")
