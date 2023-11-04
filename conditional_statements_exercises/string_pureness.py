# number_sting = int(input())
# for sentence in range(number_sting):
#     string = input()
#     for letter in string:
#         if letter == "_" or letter == ","\
#                 or letter == ".":
#             print(f"{string} is not pure!")
#             break
#     else:
#         print(f"{string} is pure.")

number_of_string = int(input())
for string in range(number_of_string):
    current_string = input()
    if "," in current_string or "." in \
            current_string or "_" in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")
