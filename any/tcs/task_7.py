'''
Задача 7
Роберт получил в наследство робота-дровосека, который умеет выполнять две операции: добавь 3, увеличь в 4 раза. Выполняя первую команду, робот колет +3 полена дров, выполняя вторую, увеличивает общее количество дров в 4 раза. Роберт хочет понять, за какое минимальное количество операций робот может получить количество дров Y, если изначальное число дров X.

Входные данные
Первая и единственная строка содержит 1 \leqslant X \leqslant Y\leqslant1001⩽X⩽Y⩽100
Результат работы
Выведите единственное число – минимальное количество операций для получения из X дров Y дров. Если это невозможно, выведите -1.

Примеры
Входные данные
10 19
Результат работы
3
'''

def supplement(str, n):
    while len(str) < n:
        str = '0' + str
    return str

nn = 5
n = nn + 1
b = range(2 ** (n) - 1)

actions_list = [bin(i)[2:] for i in b]

for i in range(len(actions_list)):
    if len(actions_list[i]) < n:
        for y in range(n):
            actions_list.append(supplement(actions_list[i], y))

actions_list = set(actions_list + [bin(i)[2:] for i in b])
actions_list = list(filter(lambda x: len(x) <= nn, actions_list))

results = []

plus_value = 3
mult_value = 4

# for actions in actions_list:
#     for start in range(3):
#         x = start
#         for action in actions:
#             print(x)
#             if x > 100:
#                 break
#             if action == '0':
#                 x += plus_value
#             else:
#                 x *= mult_value
#             sss = '{}_{}_{}'.format(start, x, actions)
#         results.append(sss)

for start in range(3):
    for actions in actions_list:
        x = start
        for action in actions:
            if x > 100:
                # if
                x = start
                break

            if action == '0':
                x += plus_value
            elif action == '1':
                x *= mult_value

        sss = '{}_{}_{}'.format(start, x, actions)
        results.append(sss)





x = 10
y = 19

# x, y = input().split(' ')
results = sorted(results, key=lambda x: (int(x.split('_')[0]), int(x.split('_')[1])))
for i in results:
    # if i.startswith('0'):
    print(i)
results = list(filter(lambda z: z.split('_')[0] == str(x) and z.split('_')[1] == str(y), results))
print(results)
results = list(map(lambda z: len(z.split('_')[2]), results))

if len(results) > 0:
    print(min(results))
else:
    print('-1')


