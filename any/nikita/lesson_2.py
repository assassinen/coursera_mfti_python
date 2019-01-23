# m = int(input())
# n = int(input())
#
matrix = []

for i in range(m):
    matrix.append([])
    for j in range(n):
        matrix[i].append(input())
#
# for i in range(m):
#     print(' '.join(matrix[i]))
#
# new_matrix = []
# for i in range(n):
#     new_matrix.append([])
#     for j in range(m):
#         new_matrix[i].append(matrix[j][i])
#
# for i in range(n):
#     print(' '.join(new_matrix[i]))
#



# m = int(input())
# n = int(input())
#
# matrix = []
# matrix_1 = []
# for i in range(n*m):
#     x = input()
#     matrix.append(x)
#     if i % 2 == 0:
#         matrix_1.insert(-(len(matrix_1)//2), x)
#     else:
#         matrix_1.append(x)
#
# matrix.reverse()
# matrix_1.reverse()
# print(matrix_1)
# print(matrix)
#
# for i in range(m):
#     for j in range(n):
#         print(matrix.pop(), end=' ')
#     print()
#
#
# for i in range(n):
#     for j in range(m):
#         print(matrix_1.pop(), end=' ')
#     print()

# n = [1,2]
# # n.append(3)
# n.insert(-1, 3)
# print(n)

# tr = [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1]
# ]
#
# for i in tr:
#     for j in i:
#         print(j, end=" ")
#     print()

tr = [
    [1]
]

n = 8
while n > 1:
    n -= 1
    last_str = tr[-1]
    tr.append([])

    new_str = tr[-1]
    new_str.append(1)
    for i in range(len(last_str)):
        if i > 0:
            new_str.append(last_str[i] + last_str[i-1])
    new_str.append(1)




for i in tr:
    for j in i:
        print(j, end=' ')
    print()
    # print(' '.join(list(map(str, i))))

#
# mediana = [6, 2, 5, 4, 3, 6, 6]
#
# f = {i:mediana.count(i) for i in mediana}
# print(sorted(f, key=lambda x: f[x], reverse=True)[0])

# print(f)

# mediana = [5, 17, 3, 9, 14, 2]
# mediana = [5, 2, 18, 8, 3]
# mediana.sort()
# if len(mediana) % 2 == 0:
#     n = len(mediana)//2
#     print((mediana[n]+mediana[n-1])//2)
# else:
#     print(mediana[len(mediana)//2])
#

