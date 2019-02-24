s = ''' 2 2 1 0 2 4 4 1 1 2 0 1 1 3 2 4 1 2 2 0 1 0 2 4 2'''
l = s.split()
print(l)


m = []
for i in range(1,6):
    m.append(l[5*i-5: 5*i])
    print(5*i-5, 5*i)
print(m)