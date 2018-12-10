import random
import math

def task_1():
    m, n = 5, 4
    matrix = [
        [random.randrange(10) for y in range(m)]
        for x in range(n)
    ]

    res = []
    print('Исходная матрица: ')
    for i in matrix:
        res.append(max(i))
        print(i)
    print()
    print('Искомая последовательность:')
    print(res)



def get_diagonal(q, n, up=False, reverse=False):
    count = [i for i in range(1, n+1)]
    start = 0
    diagonal_list = []
    for i in count:
        end = start + i
        if up:
            diagonal_index = [x-1 for x in range(n, n - i, -1)]
        else:
            diagonal_index = [x for x in range(i)]
        index_dict = list(zip(diagonal_index, reversed(diagonal_index)))
        if reverse:
            diagonal_data = dict(zip(index_dict, reversed(q[start: end])))
        else:
            diagonal_data = dict(zip(index_dict, q[start: end]))
        reverse = not reverse
        diagonal_list.append(diagonal_data)
        start += i
    return diagonal_list

def task_2():

    m, n = 5, 5
    matrix = [
        [random.randrange(10) for y in range(m)]
        for x in range(n)
    ]


    q = [i for i in range(1, m*n+1)]
    # q = [random.randrange(10, 99) for y in range(64)]
    q_n = sum([i for i in range(1, m+1)])
    print(q_n)

    diagonals = get_diagonal(q, n=n)
    for diagonal in diagonals:
        for k, w in diagonal.items():
            matrix[k[0]][k[1]]=w

    q1 = list(reversed(q[q_n:]))
    diagonals = reversed(get_diagonal(q1, n=n, up=True))
    for diagonal in diagonals:
        for k, w in diagonal.items():
            matrix[k[0]][k[1]]=w

    print('Исходная последовательность:')
    print(q)
    print()
    print('Результирующая матрица:')

    for i in matrix:
        print(i)


def task_3():
    m, n = 3, 3
    matrix = [
        [random.randrange(9) for y in range(m)]
        for x in range(n)
    ]
    i = 1
    for k in range(n):
        x = k
        y = 0
        while x >= 0:
            matrix[x][y] = i
            i += 1
            x -= 1
            y += 1

    for k in range(1, n):
        x = n-1
        y = k
        while y < n:
            matrix[x][y] = i
            i += 1
            x -= 1
            y += 1


    for i in matrix:
        print(i)



if __name__ == "__main__":
    # print('Задача #1')
    # task_1()
    # print()
    print('Задача #2')
    task_2()
    print()
    task_3()