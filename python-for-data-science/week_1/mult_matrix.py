# A = [
#     [1, 2],
#     [2, 4],
#     [3, 5]
# ]
#
# A1 = [
#     [1, 2],
#     [2, 4]
# ]

A = [[0, 9, 19, 13],
     [1, 20, 5, 13],
     [12, 11, 3, 4]]


A1 = [ [2, 0, 0, 0],
       [1, 2, 2, 0],
       [2, 1, 1, 0],
       [0, 0, 1, 1]]

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
A1 = list(zip(*A1))

for row in A1:
    for i in row:
        print('{: ^3.0f}'.format(i), end='')
    print()

print()

matrix = []
for rowA in A:
    # row = []
    # for rowA1 in A1:
    #     # print(rowA, rowA1)
    #     row.append(sum(map(lambda x, y: x * y, rowA, rowA1)))
    # print([list(map(lambda x, y: x * y, rowA, rowA1)) for rowA1 in A1])
    row = [sum(map(lambda x, y: x * y, rowA, rowA1)) for rowA1 in A1]
    matrix.append(row)

for row in matrix:
    for i in row:
        print('{: >5.0f}'.format(i), end='')
    print()

print()