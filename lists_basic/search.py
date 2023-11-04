number_strings = int(input())
key_word = input()
list_strings = []
key_list_strings = []


for string in range(number_strings):
    current_string = input()
    list_strings.append(current_string)
    if key_word in current_string:
        key_list_strings.append(current_string)
print(list_strings)
print(key_list_strings)
