list_type_fires = input().split("#")
water_litters_capacity = int(input())

HIGH_FIRE = "High"
MEDIUM_FIRE = "Medium"
LOW_FIRE = "Low"

total_efforts = 0
total_fire = 0
total_fire_putout = []

for element in list_type_fires:
    current_element = element.split("=")
    type_fire = current_element[0].strip()
    fire_force = int(current_element[1])
    current_effort = 0
    if (water_litters_capacity - fire_force) >= 0:
        filter_condition = (
                (type_fire == HIGH_FIRE and (81 <= fire_force <= 125)) or
                (type_fire == MEDIUM_FIRE and (51 <= fire_force <= 80)) or
                (type_fire == LOW_FIRE and (1 <= fire_force <= 50))
        )
        if filter_condition:
            water_litters_capacity -= fire_force
            total_fire += fire_force
            current_effort += fire_force * 25 / 100
            total_efforts += current_effort
            total_fire_putout.append(fire_force)
print("Cells:")
for every_fire in total_fire_putout:
    print(f"- {every_fire}")

print(f"Effort: {total_efforts:.2f}")
print(f"Total Fire: {total_fire}")
