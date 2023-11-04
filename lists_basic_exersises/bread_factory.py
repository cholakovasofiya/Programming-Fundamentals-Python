events = input().split("|")
energy = 100
coins = 100
factory_is_open = True

for element in events:
    current_event = element.split("-")
    event_type = current_event[0]
    event_value = int(current_event[1])
    if event_type == "rest":
        current_energy = energy
        energy += event_value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event_type == "order":
        if energy >= 30:
            energy -= 30
            coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= event_value:
            coins -= event_value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            factory_is_open = False
            break
if factory_is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
