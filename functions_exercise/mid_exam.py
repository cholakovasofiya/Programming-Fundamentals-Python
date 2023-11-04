vacation_days = int(input())
budget_group = float(input())
number_people = int(input())
fuel_price_km = float(input())
food_expenses_person_day = float(input())
hotel_price_night = float(input())
distance = input().split()
fuel_expenses = []

accommodation = number_people * hotel_price_night * vacation_days
food = number_people * food_expenses_person_day * vacation_days

if number_people > 10:
    accommodation -= 0.25 * accommodation

for trip in distance:
    current_trip = int(trip) * fuel_price_km
    fuel_expenses.append(current_trip)
index = 0

current_costs = accommodation + food
for day in range(1, vacation_days + 1):
    fuel = fuel_expenses[index]
    current_costs += fuel
    if day % 3 == 0 or day % 5 == 0:
        current_costs += 0.40 * current_costs
    if day % 7 == 0:
        current_costs -= current_costs / number_people
    if budget_group < current_costs:
        print(f"Not enough money to continue the trip. You need {current_costs - budget_group:.2f}$ more.")
        break
    index += 1
if budget_group >= current_costs:
    print(f"You have reached the destination. You have {budget_group - current_costs:.2f}$ left.")
