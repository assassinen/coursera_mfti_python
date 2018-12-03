import random
# Под цифрой 5 в каждом задании.


def task_1():
    print('task_1')
    '''5. Дан одномерный массив из случайных целых чисел, насчитывающий N элементов.
    Вставить группу из M новых элементов, начиная с No i. '''
    n = range(random.randrange(5, 10))
    m = range(random.randrange(5, 10))
    i = random.randrange(len(n))
    old_array = [random.randrange(10) for y in n]
    new_array = [random.randrange(10) for y in m]
    array = old_array[:i] + new_array + old_array[i:]
    print(f'{old_array} - массив из N элементов')
    print(f'{new_array} - массив из M элементов')
    print(f'{i} - позиция для вставки')
    print(f'{array} - полученный массив')


def task_2():
    print()
    print('task_2')
    '''5. Заданы М строк слов, которые вводятся с клавиатуры.
    Вводится слог (последовательность букв). Удалить данный слог из каждой строки.'''
    string = \
'''В недрах тундры
Выдры в гетрах
Тырят в вёдра
Ядра кедров!

Выдрав с выдры
В тундре гетры
Вытру выдрой ядра кедров
Вытру гетрой выдре морду
Ядра в вёдра
Выдру в тундру!
    '''
    syllable = 'кедр'
    new_string=string.replace(syllable, '')
    print('Исходная строка:')
    print(string)
    print(f'Слог: {syllable}')
    print()
    print('Новая строка:')
    print(new_string)


def task_3():
    print()
    print('task_3')
    '''5. Выполнить обработку элементов прямоугольной матрицы А, имеющей N строк и М столбцов.
    Определить средние значения по всем строкам и столбцам матрицы.
    Результат оформить в виде матрицы из N+1 строк и М+1 столбцов (исходная матрица + средние значения по строкам и столбцам).'''

    m, n = 2, 2
    matrix = [
        [round(float(random.randrange(1, 10)), 2) for y in range(m)]
        for x in range(n)
    ]
    print('Было:')
    for row in matrix:
        print(row)

    for row in matrix:
        row.append(round(sum(row)/len(row), 2))

    avg_row = []
    for col_idx in range(len(matrix[0])):
        avg = []
        for row in matrix:
            avg.append(row[col_idx])
        avg_row.append(round(sum(avg)/len(avg), 2))
    matrix.append(avg_row)
    print('Стало:')
    for row in matrix:
        print(row)


def task_4():
    '''5. Подсчитать количество студентов, не сдавших два экзамена. Вывести номера этих студентов.'''
    print()
    print('task_4')
    m, n = 4, 5
    STUD = [
        [random.randrange(2, 5) for y in range(m)]
        for x in range(n)
    ]
    print("Ведомость:")
    losers = []
    i = 1
    for row in STUD:
        if row.count(2) > 1:
            losers.append(str(i))
        i += 1
        print(row)

    print(f'Количество студентов не сдавших два экзамена = {len(losers)}')
    print('Их номера: ', ', '.join(losers))



if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
