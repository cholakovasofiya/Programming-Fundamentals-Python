def factorial(num):
    factorial_number = 1
    for i in range(1, num+1):
        factorial_number = factorial_number * i
    return factorial_number


first_number_input = int(input())
second_number_input = int(input())
result = factorial(first_number_input) / factorial(second_number_input)
print(f"{result:.2f}")
