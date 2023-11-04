number_of_orders = int(input())
total_price = 0

for order in range(number_of_orders):
    capsule_price = float(input())
    number_of_days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= capsule_price <= 100 and 1 <= number_of_days <= 31\
            and 1 <= capsules_per_day <= 2000:
        coffee_price = capsule_price * number_of_days * capsules_per_day
        total_price += coffee_price
    else:
        continue
    print(f"The price for the coffee is: ${coffee_price:.2f}")
print(f"Total: ${total_price:.2f}")
