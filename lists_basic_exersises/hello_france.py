import math

ticket_train = 150
MAX_PRICE_CLOTHES = 50
MAX_PRICE_SHOES = 35
MAX_PRICE_ACCESSORIES = 20.50
profit = 0
money_spent_items = 0

list_items = input().split("|")
budget = float(input())

list_items_profit = []

for element in list_items:
    current_element = element.split("->")
    item = current_element[0]
    item_price = float(current_element[1])
    if budget >= item_price:
        item_plus_profit = 0
        item_profit = 0
        filter_condition = (
                (item == "Clothes" and item_price <= MAX_PRICE_CLOTHES) or
                (item == "Shoes" and item_price <= MAX_PRICE_SHOES) or
                (item == "Accessories" and item_price <= MAX_PRICE_ACCESSORIES)
        )
        if filter_condition:
            budget -= item_price
            money_spent_items += item_price
            item_profit += item_price * (40 / 100)
            profit += item_profit
            item_plus_profit += (item_price + item_profit)
            list_items_profit.append(item_plus_profit)
for element in list_items_profit:
    print(f"{element:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")

budget_ticket = budget + profit + money_spent_items
if budget_ticket >= ticket_train:
    print("Hello, France!")
else:
    print("Not enough money.")


# with round function
# import math
#
# ticket_train = 150
# MAX_PRICE_CLOTHES = 50
# MAX_PRICE_SHOES = 35
# MAX_PRICE_ACCESSORIES = 20.50
# profit = 0
# money_spent_items = 0
#
# list_items = input().split("|")
# budget = float(input())
#
# list_items_profit = []
#
# for element in list_items:
#     current_element = element.split("->")
#     item = current_element[0]
#     item_price = float(current_element[1])
#     if budget >= item_price:
#         item_plus_profit = 0
#         item_profit = 0
#         filter_condition = (
#                 (item == "Clothes" and item_price <= MAX_PRICE_CLOTHES) or
#                 (item == "Shoes" and item_price <= MAX_PRICE_SHOES) or
#                 (item == "Accessories" and item_price <= MAX_PRICE_ACCESSORIES)
#         )
#         if filter_condition:
#             budget -= item_price
#             money_spent_items += item_price
#             item_profit += item_price * (40 / 100)
#             profit += round(item_profit, 2)
#             item_plus_profit += round(item_price + item_profit, 2)
#             list_items_profit.append(item_plus_profit)
# print(*list_items_profit)
# print(f"Profit: {profit}")
# budget_ticket = budget + profit + money_spent_items
# if budget_ticket >= ticket_train:
#     print("Hello, France!")
# else:
#     print("Not enough money.")
