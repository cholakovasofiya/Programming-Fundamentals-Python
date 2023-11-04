# function which return reverse of a string

# def isPalindrome(s):
#     return s == s[::-1]

def palindrome(lst):
    lst_numbers = []
    for element in lst:
        if element == element[::-1]:
            lst_numbers.append("True")

        else:
            lst_numbers.append("False")
    return lst_numbers


lst_numbers_input = input().split(", ")
lst_numbers = palindrome(lst_numbers_input)
for string in lst_numbers:
    print(string)
