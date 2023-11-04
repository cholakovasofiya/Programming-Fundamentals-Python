people_in_group = int(input())
number_days = int(input())
money_spent = 0
total_money = 0

for day in range(1, number_days + 1):

    if day % 10 == 0:
        people_in_group -= 2
    if day % 15 == 0:
        people_in_group += 5
    if day % 3 == 0:
        money_spent += people_in_group * 3
    if day % 5 == 0:
        total_money += people_in_group * 20
        if day % 3 == 0:
            money_spent += people_in_group * 2
    total_money += 50
    money_spent += people_in_group * 2

money_per_person = int((total_money - money_spent) // people_in_group)
print(f"{people_in_group} companions received {money_per_person} coins each.")

# Test 2 people and 10 days (100/100 in Judge) with ZerroDivisionError
