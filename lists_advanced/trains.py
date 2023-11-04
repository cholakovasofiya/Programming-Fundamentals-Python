number_wagons = int(input())
train = [0] * number_wagons
while True:
    command = input().split()

    if command[0] == "End":
        break
    elif command[0] == "add":
        people = int(command[1])
        train[-1] += people
    elif command[0] == "insert":
        index, people = int(command[1]), int(command[2])
        train[index] += people
    elif command[0] == "leave":
        index, people = int(command[1]), int(command[2])
        train[index] -= people
print(train)
