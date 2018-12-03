import random

#а) Дана действительная матрица размера m x n.
# Найти сумму наибольших значений элементов её строк.

m, n = 10, 10
matrix = [
    [random.randrange(10) for y in range(m)]
    for x in range(n)
]

matrix[2] = [random.randrange(1, 10, 2) for y in range(m)]

max_row_items = []
for row in matrix:
    max_row_items.append(max(row))

print('Матрица:')
for row in matrix:
    print(row)
print(f'Cумма наибольших значение элементов строк матрица равна {sum(max_row_items)}')


#б) По матрице А(10, 10) построить массив В(10) по правилу:
# В(I) присвоить 1, если в строке с номером I матрицы А есть хотя бы один четный элемент, и значение 0 – в противном случае.

B = []
for row in matrix:
    B_items = 0
    for item in row:
        if item % 2 == 0:
            B_items = 1
    B.append(B_items)
print(f'Массив: {B}')


