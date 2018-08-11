# a = {'another_key_#_1503319740': '10', 'another_key_#_1503319744': '10', 'key_#_150331977': '10'}
# s = []
# b = [(k.split('_#_')[0], i, k.split('_#_')[1], '\n') for k, i in a.items() if k.split('_#_')[0] == 'another_key']
# for i in b:
#     s.append(' '.join(i))
# print(b)
# print(''.join(s))

def sum_(n):
    sum = 0
    while n > 0:
        d = n % 10
        n = n // 10
        sum += d
    return sum

s = (i for i in range(1, 1001) if i % 3 == 0 and i % 5 != 0 and sum(map(int, str(i))) < 10)
print(next(s))
print(next(s))
print(next(s))
print(next(s))

# s = 123
# print(str(s).split())
# def gen():
#     i = 0
#     y = 1
#     while True:
#         i, y = y, y + i
#         yield i
#
#
#
# n = gen()
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))



