command = input()
counter_coffee = 0
while command != "END":
    if command.lower() == "coding" or command.lower() == "dog" \
            or command.lower() == "cat" or\
            command.lower() == "movie":
        counter_coffee += 1
        if command.isupper():
            counter_coffee += 1
    if counter_coffee >= 5:
        print("You need extra sleep")
        break
    command = input()
if command == "END":
    print(counter_coffee)
