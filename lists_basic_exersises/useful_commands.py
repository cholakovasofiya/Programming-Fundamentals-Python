# my_list = [2, 3, 6, 9, 45, 7, 2]
# my_letters_list = ['a', 'b', 'c', 'd']
#
# my_letters_list.sort(reverse=True)
# print(my_letters_list)
#
# # symbols and numbers
# print(sorted([5, 7, 67, 8, 46, 789]))
#
# # delete the last element and keep it in variable
# char = my_list.pop()
# print(my_list)
# print(char)
#
# # index insert value
# my_letters_list = ['a', 'b', 'c', 'd']
# my_list.insert(5, "Pesho")
#
# # first coincidence in the list
# my_list = [2, 3, 6, 9, 45, 7, 2]
# number = my_list.index(2)
# print(number)
#
#
# # only one 2 left in the list
# repetition = my_list.count(2)
# while my_list.count(2) > 1:
#     my_list.remove(2)
# print(my_list)

# # indexes with number 2
# my_list = [2, 3, 6, 9, 45, 7, 2]
# indexes = []
# for index, element in enumerate(my_list):
#     if int(element) == 2:
#         indexes.append(index)
# print(indexes)


# my_list = [2, 3, 6, 9, 45, 7, 2]
# my_list.reverse()
# print(my_list)
# print(my_list[::-1])

#
# my_list = [2, 3, 6, 9, 45, 7, 2]
# my_second_list = my_list
# my_second_list.remove(2)
# print(my_list)
# print(my_second_list)

# clone the list
my_list = [2, 3, 6, 9, 45, 7, 2]
my_second_list = my_list.copy()
my_second_list.remove(2)
print(my_list)
print(my_second_list)


# A = [1,2,3,4,5,6] split the list in two
# B = A[:len(A)//2]
# C = A[len(A)//2:]

# list_numbers_digits.sort() sorting the list ASC


# print the value of the list without brackets
# if the value is int but not str
print(', '.join(map(str, list_numbers_digits)))
print(*list_numbers_digits, sep=',')


# double split
# events = input().split("|")
# for element in events:
#     current_event = element.split("-")
#     event_type = current_event[0]
#     event_value = int(current_event[1])


#     if item == "Cloths=":
#         if item_price <= MAX_PRICE_CLOTHES:
#             item_price += 40 / 100
#
#     elif item == "Shoes":
#         if item_price <= MAX_PRICE_SHOES:
#             item_price += 40 / 100
#
#     elif item == "Accessories":
#         if item_price <= MAX_PRICE_ACCESSORIES:
#             item_price += 40 / 100
#     profit += item_price
#     budget += item_price
# print(f"Profit: {profit}")


# print("Rounding 3.367824 upto 2 decimal places:",  roundedNumber)
# Rounding 3.367824 upto 2 decimal places: 3.37


# filter_conditions
# filter_condition = (
#         (command == COMMAND_EVEN and number % 2 == 0) or
#         (command == COMMAND_ODD and number % 2 != 0) or
#         (command == COMMAND_POSITIVE and number >= 0) or
#         (command == COMMAND_NEGATIVE and number < 0)
#     )
#     if filter_condition:
#         filtered_numbers.append(number)