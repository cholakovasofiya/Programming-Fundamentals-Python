gifts = input().split()
command = input().split()
OUT_OF_STOCK = "OutOfStock"
REQUIRED = "Required"
JUST_IN_CASE = "JustInCase"

while command != "No Money":
    for element in command:
        current_command = element[0]
        current_element = element[1]
        
        if current_command == OUT_OF_STOCK:
            current_element = None
        elif current_command == REQUIRED:
            pass
    print(gifts)

    command = input().split()
