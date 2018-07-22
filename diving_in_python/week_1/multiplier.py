#/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import random
from datetime import datetime
import time
import sys
import signal

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def nonBlockingInput(prompt='', timeout=2):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = input(input_str)
        signal.alarm(0)
        return text
    except AlarmException:
        print('\nДолго нет ответа. Попробуйте учить, а не считать.')
    signal.signal(signal.SIGALRM, signal.SIG_IGN)



start = int(sys.argv[1])
stop = int(sys.argv[2])
n = nn = int(sys.argv[3])
timeout = int(sys.argv[4])
t = str(datetime.now())

f = open('text.txt', 'a')
f.write('\n')
f.write("start test:" '\n' + str(t) + '\n')
rez = [0,0,0]
input_list = set()

while n > 0:
    x = random.randint(start, stop)
    y = random.randint(1, 10)
    n -= 1

    input_str = str(x) + " * " + str(y) + " = "

    while input_str in input_list:
        x = random.randint(start, stop)
        y = random.randint(1, 10)
        input_str = str(x) + " * " + str(y) + " = "

    input_list.add(input_str)

    z = nonBlockingInput(timeout = timeout)

    if z is None :
        rez[2] = rez[2] + 1
        continue
    elif z.isdigit():
        z = int(z)
    else:
        print("Ответ не является числом.")
        input_list.pop()
        n += 1
        continue
    f.write(input_str + str(z) + '\n')
    if z == x * y:
        rez[0] = rez[0] + 1
        print("Верно.")
    else:
        rez[1] = rez[1] + 1
        print("Не верно.")

f.write("Верно - " + str(rez[0]) + " из " + str(nn) + '\n')
f.write("Не верно - " + str(rez[1]) + " из " + str(nn) + '\n')
f.write("Нет ответа - " + str(rez[2]) + " из " + str(nn) + '\n')
f.write("Оценка - " + str(int(5 * rez[0] / nn)) + '\n')
f.close()
print("Оценка - " + str(int(5 * rez[0] / nn)))


