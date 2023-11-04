count_of_buckets = int(input())
tank_capacity = 255
poured_litters = 0

for bucket in range(count_of_buckets):
    litters_of_water = int(input())
    if litters_of_water > tank_capacity:
        print("Insufficient capacity!")
    else:
        tank_capacity -= litters_of_water
        poured_litters += litters_of_water
print(poured_litters)
