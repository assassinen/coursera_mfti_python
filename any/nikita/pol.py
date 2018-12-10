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
a = '''
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

# b = set(a.lower().split())
# print([i for i in a.lower().strip().split()])
# print(type(a.lower().strip('\n')))
# c = []
# # for i in a:
# #     print(i)
# answer = []
# for i in b:
#     c.append(a.count(i))
# for i in b:
#     if a.count(i) == max(c):
#         answer.append(i)
# print(' '.join(sorted(answer)))


# Господа! Я собрал вас здесь, чтобы сообщить вам пренеприятнейшее известие...
# Господа!
# Я
# собрал
# вас
# здесь,
# чтобы
# сообщить
# вам
# пренеприятнейшее
# известие...

a = input().lower()
b = set(a)
b.remove(' ')

c = []
answer = []
for i in b:
    c.append(a.count(i))
for i in b:
    if a.count(i) == max(c):
        answer.append(i)
print(' '.join(sorted(answer)))