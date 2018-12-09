import random

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



def get_diagonal(q, up=False, reverse=False):
    n = 8
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
    global matrix
    m, n = 8, 8
    matrix = [
        [random.randrange(10) for y in range(m)]
        for x in range(n)
    ]

    # q = [i for i in range(1, 65)]
    q = [random.randrange(10, 99) for y in range(64)]

    diagonals = get_diagonal(q)
    for diagonal in diagonals:
        for k, w in diagonal.items():
            matrix[k[0]][k[1]]=w

    q1 = list(reversed(q[36:]))
    diagonals = reversed(get_diagonal(q1, up=True))
    for diagonal in diagonals:
        for k, w in diagonal.items():
            matrix[k[0]][k[1]]=w

    print('Исходная последовательность:')
    print(q)
    print()
    print('Результирующая матрица:')

    for i in matrix:
        print(i)




if __name__ == "__main__":
    print('Задача #1')
    task_1()
    print()
    print('Задача #2')
    task_2()