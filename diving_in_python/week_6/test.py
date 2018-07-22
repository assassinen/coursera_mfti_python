a = {'another_key_#_1503319740': '10', 'another_key_#_1503319744': '10', 'key_#_150331977': '10'}
s = []
b = [(k.split('_#_')[0], i, k.split('_#_')[1], '\n') for k, i in a.items() if k.split('_#_')[0] == 'another_key']
for i in b:
    s.append(' '.join(i))
print(b)
print(''.join(s))