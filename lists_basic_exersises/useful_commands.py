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
round(2.5)
round(3.5)

# delete file.py
# import os
# os.remove("name_of_the_file")

# tkinter - for frames
# basic calculator
# def intro():
#     return '''##################################
# # Welcome to SoftUni Calculator  #
# #   Please select an option to   #
# #          continue              #
# #                                #
# #                                #
# #   Author: Mario Zahariev       #
# #   Course: SoftUni Fundamentals #
# #                                #
# ##################################\n'''
#
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# print(intro())
#
# while True:
#     choice = input('1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\nEnter your choice: ')
#
#     if choice == '5':
#         print('Thank you for using our calculator!!!')
#         break
#
#     if choice == '1':
#         n1 = float(input('Enter first number: '))
#         n2 = float(input('Enter second number: '))
#         print('The sum is: ', add(n1, n2), '\n')
#
#     elif choice == '2':
#         n1 = float(input('Enter first number: '))
#         n2 = float(input('Enter second number: '))
#         print('The result of the subtract is: ', subtract(n1, n2), '\n')
#
#     elif choice == '3':
#         n1 = float(input('Enter first number: '))
#         n2 = float(input('Enter second number: '))
#         print('The sum is: ', multiply(n1, n2), '\n')
#
#     elif choice == '4':
#         n1 = float(input('Enter first number: '))
#         n2 = float(input('Enter second number: '))
#         print('The sum is: ', divide(n1, n2), '\n')
#
#     else:
#         print('Wrong choice!!!\n')
#
# # 1.	Absolute Values
# numbers = input().split(' ')
# abs_numbers = []
#
# for num in numbers:
#     abs_numbers.append(abs(float(num)))
#
# print(abs_numbers)
#
#
# # numbers = list(map(float, input().split(' ')))
# # result = [abs(num) for num in numbers]
# # print(result)
#
# # 2.	Grades
# def type_of_grade(score):
#     if 2.00 <= score <= 2.99:
#         return 'Fail'
#     elif 3.00 <= score <= 3.49:
#         return "Poor"
#     elif 3.50 <= score <= 4.49:
#         return "Good"
#     elif 4.50 <= score <= 5.49:
#         return "Very Good"
#     elif 5.50 <= score <= 6.00:
#         return "Excellent"
#
#
# score = float(input())
# print(type_of_grade(score))
#
#
# # 3.	Calculations
# def calculation_func(number_a, number_b, operation):
#     if operation == "multiply":
#         return number_a * number_b
#
#     elif operation == "divide":
#         return int(number_a / number_b)
#
#     elif operation == "add":
#         return number_a + number_b
#
#     elif operation == "subtract":
#         return number_a - number_b
#
#
# type_of_operation = input()
# first_number = int(input())
# second_number = int(input())
# print(calculation_func(first_number, second_number, type_of_operation))
#
# # 4.	Repeat String
# string = input()
# number = int(input())
# result = lambda string, num: string * num
# print(result(string, number))
#
# # 7.	Rounding
# result = list(map(lambda x: round(float(x)), input().split(' ')))
#
# print(result)


# recursion
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)
#
# def func_dock_string():
#     '''
#
#     :param
#     :return:
#     '''