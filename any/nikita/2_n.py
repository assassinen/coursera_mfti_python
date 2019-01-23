h = int(input())
n = int(input())
table = []
for i in range(h):
    row = []
    for j in range(n):
        row.append(input())
    table.append(row)
for element in table:
    print('\t'.join(element))

# table = []
print()

future = []
# for i in range(h):
#     row = []
#     counter = 0
#     for j in range(n):
#         row.append(table[j][i])
#         counter += 1
#     future.append(row)
#
# for element in future:
#     print('\t'.join(element))

print(table)
for i in range(n):
    for k in range(h):
        print(table[k][i])
    print()
#
#
#
# h = int(input())
# n = int(input())
# table = []
# for i in range(h):
#     row = []
#     for j in range(n):
#         row.append(input())
#     table.append(row)
# for element in table:
#     print('\t'.join(element))
# print()
# future = []
# for i in range(n):
#     row = []
#     for j in range(h):
#         row.append(table[i][i])
#         future.append(row)
# for element in future:
#     print('\t'.join(element))