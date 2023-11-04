def string_ascii(char1, char2):
    list_characters = []
    for character in range(ord(char1) + 1, ord(char2)):
        list_characters.append(chr(character))
    return list_characters


first_char = input()
second_char = input()
print(' '.join(string_ascii(first_char, second_char)))
