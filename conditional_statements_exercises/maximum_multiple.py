number_divisor = int(input())
number_boundary = int(input())

for num in range(number_boundary, -1, -1):
    if num % number_divisor == 0:
        print(num)
        break
