given_numbers = input().split(" ")
given_numbers_integers = []


def rounding():
    for element in given_numbers:
        current_element = float(element)
        given_numbers_integers.append(round(current_element))
    print(given_numbers_integers)


rounding()
