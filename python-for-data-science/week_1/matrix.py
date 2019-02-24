A = [
    [2, 1, -3],
    [1, 0, 0],
    [1, 0, 1]
]

A1 = [
    [0, 1, 0],
    [1, -5, 3],
    [0, -1, 1]
]

for row in A:
    for i in row:
        print('{: ^3.0f}'.format(i), end='')
    print()

print()

for row in A1:
    for i in row:
        print('{: ^3.0f}'.format(i), end='')
    print()

print()
z = list(zip(*A1))

for row in z:
    for i in row:
        print('{: ^3.0f}'.format(i), end='')
    print()

print()

for rowA in A:
    for rowA1 in A1:
        # print(rowA, rowA1)
        print(list(map(lambda x, y: x * y, rowA, rowA1)))