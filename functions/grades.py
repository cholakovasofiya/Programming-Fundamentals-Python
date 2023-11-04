current_grade = float(input())


def grades(grade):
    if grade >= 5.50:
        print("Excellent")
    elif grade >= 4.50:
        print("Very Good")
    elif grade >= 3.50:
        print("Good")
    elif grade >= 3.00:
        print("Poor")
    elif grade <= 2.99:
        print("Fail")


grades(current_grade)
