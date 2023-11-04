count_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_shield = 0
expenses_repair = 0

for fight in range(1, count_lost_fights + 1):
    if fight % 2 == 0:
        expenses_repair += helmet_price
    if fight % 3 == 0:
        expenses_repair += sword_price
        if fight % 2 == 0:
            expenses_repair += shield_price
            broken_shield += 1
            if broken_shield % 2 == 0 and broken_shield > 0:
                expenses_repair += armor_price

print(f"Gladiator expenses: {expenses_repair:.2f} aureus")


# number_of_lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
# total_helmets_broken = number_of_lost_fights // 2
# total_swords_broken = number_of_lost_fights // 3
# total_shields_broken = number_of_lost_fights // 6 #number_of_lost_fights // (2+3)
# total_armors_broken = total_shields_broken // 2
# expenses = helmet_price * total_helmets_broken + \
#     sword_price * total_swords_broken + \
#     shield_price * total_shields_broken + \
#     armor_price * total_armors_broken
# print(f"Gladiator expenses: {expenses:.2f} aureus")
