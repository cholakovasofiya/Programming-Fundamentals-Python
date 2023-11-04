import math
number_of_people = int(input())
capacity = int(input())

number_of_courses = math.ceil(number_of_people/capacity)
print(number_of_courses)

# number_of_full_courses = number_of_people // capacity
# number_of_last_course = number_of_people % capacity
#
# if number_of_people < capacity:
#     print('All the persons fit inside the '
#           'elevator.\nOnly one course is needed.')
# else:
#     if number_of_last_course < capacity:
#         print(f"{number_of_full_courses} courses * {capacity} "
#               f"people\n+ 1 course * {number_of_last_course} "
#               f"persons")
#     else:
#         print(f"{number_of_full_courses} courses * {capacity}"
#               f"people")


