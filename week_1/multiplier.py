#/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import random
from datetime import datetime
import sys

start = int(sys.argv[1])
stop = int(sys.argv[2])
n = nn = int(sys.argv[3])
t = str(datetime.now())

f = open('text.txt', 'a')
f.write('\n')
f.write("start test:" '\n' + str(t) + '\n')
rez = [0,0]

while n > 0:
    x = random.randint(start, stop)
    y = random.randint(1, 10)
    n -=1

    z = input(str(x) + " * " + str(y) + " = ")
    if z.isdigit():
        z = int(z)
    else:
        print("Ответ не является числом.")
        n += 1
        continue
    f.write(str(x) + " * " + str(y) + " = " + str(z) + '\n')
    if z == x * y:
        rez[0] = rez[0] + 1
        print("Верно.")
    else:
        rez[1] = rez[1] + 1
        print("Не верно.")

f.write("Верно - " + str(rez[0]) + " из " + str(nn) + '\n')
f.write("Не верно - " + str(rez[1]) + " из " + str(nn) + '\n')
f.write("Оценка - " + str(int(5 * rez[0] / nn)) + '\n')
f.close()
print("Оценка - " + str(int(5 * rez[0] / nn)))
