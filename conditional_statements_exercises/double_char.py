string = input()
while string != "End":

    if string != "SoftUni":
        for letter in string:
            print(letter * 2, end="")

        print(end="\n")
    string = input()


