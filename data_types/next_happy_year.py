current_year = int(input())
happy_year = False

while not happy_year:
    current_year += 1
    set_year = set()
    for number in range(len(str(current_year))):
        set_year.add(str(current_year)[number])

        happy_year = len(set_year) == len(str(current_year))
print(current_year)
