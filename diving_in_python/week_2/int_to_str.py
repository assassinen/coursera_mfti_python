from _functools import reduce

l = [i for i in range(10)]

print(l)

s = list(map(str, l))

print(s)

print(reduce(lambda x, y: x * y, range(1, 5)))

print(list(filter(bool, range(3))))

print(list(zip(
  filter(bool, range(3)),
  [x for x in range(3) if x]
)))