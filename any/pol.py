# a = [7, 2, 3, '*','-']
# b = [] # наш стек
#
# for i in a:
#     if i == '*':
#         # умножить два послених элемента из стека (списка b)
#         # вставить результат с стек (в список b)
#         b.append(b.pop() * b.pop())
#     elif i == '+':
#
#         pass
#     elif i == '-':
#         x = b.pop()
#         y = b.pop()
#         b.append(y - x)
#     else:
#         b.append(i)
# print(b[0])

# text = "hello_cruel_world._This_is_a_sample_textttttt"
# l = {i:text.count(i) for i in text}
# print(sorted(l, key=lambda x: l[x], reverse=True))

s = ['s', 'a']
print(s)
print(sorted(s))

print(' '.join(s))
print(' '.join(sorted(s)))

