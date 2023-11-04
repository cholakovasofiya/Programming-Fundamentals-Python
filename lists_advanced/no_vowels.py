text_input = input().lower()
list_vowels = ['a', 'o', 'u', 'e', 'i']
final_list = [letter for letter in text_input if letter not in list_vowels]
print(''.join(final_list))
