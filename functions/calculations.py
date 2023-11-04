input_operator = input()
int_a = int(input())
int_b = int(input())


def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a // b


print(calculator(input_operator, int_a, int_b))
