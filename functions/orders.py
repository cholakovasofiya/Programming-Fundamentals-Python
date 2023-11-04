product = input()
count_products = int(input())
COFFEE = 1.50
WATER = 1
COKE = 1.40
SNACKS = 2


def sum_products():
    final_sum = 0
    if product == "coffee":
        final_sum = COFFEE * count_products
    elif product == "water":
        final_sum = WATER * count_products
    elif product == "coke":
        final_sum = COKE * count_products
    elif product == "snacks":
        final_sum = SNACKS * count_products
    print(f"{final_sum:.2f}")


sum_products()
