# a = input().split()
# b = []
#
# for i in a:
#     if i == '*':
#         b.append(b.pop() * b.pop())
#     elif i == '+':
#         b.append(b.pop() + b.pop())
#     elif i == '-':
#         x = b.pop()
#         y = b.pop()
#         b.append(y - x)
#     else:
#         b.append(int(i))
# print(b[0])

# matrix = [
#     [1, 2, 3],
#     [2, 5, 5],
#     [5, 3, 4]
# ]
#
# for i in matrix:
#     print(i)

# a = ''.join((input().lower()).split())
# print(a)

test = '''
Господа!
Я
собрал
вас
здесь,
чтобы
сообщить
вам
пренеприятнейшее
известие...'''

a = input().lower() or test
b = set(a)
for i in [' ', '\n']:
    if i in b:
        b.remove(i)


c = []
answer = []
for i in b:
    c.append(a.count(i))
for i in b:
    if a.count(i) == max(c):
        answer.append(i)
print(' '.join(sorted(answer)))

a = [6, 2, 5, 4, 3, 6, 6]

import statistics
print(statistics.mode(a))