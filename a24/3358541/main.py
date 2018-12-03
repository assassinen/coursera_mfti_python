import random
from functools import reduce

def task_1():
    print('task_1')
    students = ['Иванов', 'Петров', 'Сидоров']
    n, m = 5, 5

    def gen_grade():
        return [
            random.randrange(3, 5) for y in range(m)
        ]

    session_result = {}
    for students in students:
        session_result[students]=gen_grade()

    session_result['Васечкий']=[4, 4, 5, 5, 4]
    for k, v in session_result.items():
        print(f'{k} получил такие оценки: {v} ')

    honours_pupils = []
    for k, v in session_result.items():
        honours_pupils.append(k)
        if 1 in v or 2 in v or 3 in v:
            honours_pupils.pop()

    print(f'Количество отличников и хорошистов: {len(honours_pupils)}')
    print('Их имена:', ', '.join(honours_pupils))

def task_2():
    print()
    print('task_2')
    n = 30
    F = [random.randrange(1, 10) for y in range(n)]
    print(f'Исходные массив: {F}')
    print(f'Сумма первых десяти элеметов: {sum(F[:10])}')
    print(f'Произвение последних пяти элеметов: {reduce(lambda x, y: x * y, F[-5:])}')
    if sum(F[:10]) > reduce(lambda x, y: x * y, F[-5:]):
        print('Сумма первых десяти элеметов больше произвения последних пяти элеметов')
    elif sum(F[:10]) < reduce(lambda x, y: x * y, F[-5:]):
        print('Сумма первых десяти элеметов меньше произвения оследних пяти элеметов')
    else:
        print('Сумма первых десяти элеметов равна произвению оследних пяти элеметов')


if __name__ == "__main__":
    task_1()
    task_2()
