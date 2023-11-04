# number_patterns = int(input())
#
# for i in range(1, number_patterns + 1):
#     print(i * '*')
# for j in range(number_patterns - 1, 0, -1):
#     print(j * '*')


rows = int(input())
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')