'''
Задача 6
После просмотра мультика «Подарок для самого слабого», Роберт пустил скупую мужскую слезу и решил закинуть зайцам ящик с едой с помощью квадрокоптера. Лес, где бегают зайцы, представлен многоульником (не обязательно выпуклым). Роберт наугад вбивает координаты точки сброса ящика в квадрокоптер (которые точно не лежат на границе леса), и пока он не запустил всю эту махину наверх, надо понять, попадет ли ящик в лес (а не в поле вокруг).

Входные данные
Первая строка содержит число вершин многоугольника, описывающего лес N (3 \leqslant N \leqslant 100)N(3⩽N⩽100). Следующие N строк содержат пару вещественных чисел, задающих вершины многоугольника. Следующая строка содержит пару координат, которые Роберт вбил в квадрокоптер.
Результат работы
Выведите «YES», если координаты в квадрокоптере попадут в лес и «NO», если иначе.

Примеры
Входные данные
3
0 0
1 0
0 1
0.5 0.3
Результат работы
YES
'''

# s = {'100', '11', '1', '010', '001', '110', '0', '101', '10', '000', '011'}
#
# print(s)
# print(sorted(s, key=lambda x: len(x), reverse=False))
# # print(s)

r = ['0', '1']
s = ['0', '1']
for _ in range(3):
    for i in s:
        new = []
        for j in r:
            new.append(j + i)
            print(j)
    s.extend(new)

print(s)