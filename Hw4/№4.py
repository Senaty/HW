n = int(input('Введите число:'))
a = int(input('Введите исключаемое множество:\na:'))
b = int(input('b:'))
for i in range(n, 0, -1):
    if i % 2 == 1:
        if i <= min(a, b) or i >= max(a, b):
            print(i)
###################################################
import math

print('/////////////////////')

while 0 == 0:
    t = input('Введите команду:')
    if t == 'Лого':
        text = input('Введите строку:')
        print('ln(', len(text), ')=', math.log(len(text)))
    elif t == 'Триго':
        d = float(input('Введите число:'))
        p = math.radians(d)
        print('sin(', d, ')=', '%.4f' % math.sin(p))
        print('cos(', d, ')=', '%.4f' % math.cos(p))
        print('tg(', d, ')=', '%.4f' % math.tan(p))
        print('ctg(', d, ')=', '%.4f' % math.atan(p))
    elif t == 'Конец':
        break
    else:
        continue
##########################################################
import random

while 0 == 0:
    n = float(input('Введите число от 0 до 1000:'))
    a = random.randint(0, 1000)
    b = random.randint(a, 1000)
    if min(a, b) <= float(n) <= max(a, b):
        print('Lucky!')
    elif n < 0 or n > 1000:
        text = ['Are u stupid?!Try again!', 'TRY AGAIN!!!', 'Can u tell me, Why cant you do it right? ']
        print(random.choice(text))
        continue
    else:
        print('Try again!')
        break
#####################################################################
while 0 == 0:
    a = int(input('Введите число a: '))
    b = int(input('Введите число b: '))
    M = random.randint(a, b)
    for i in range(1, M + 1):
        print('%.3f' % math.log10(i))
    text = input('Желаете продолжить?Y/N\n')
    if text == 'Y':
        continue
    elif text == 'N':
        break
########################################################
n = int(input('Введите N'))
pi = math.pi
for i in range(1, n + 1):
    if i % 5 != 0:
        p = 2 * pi * i
        s = pi * i * i
        print('Длина окружности с радиусом', i, ':', '%.2f' % p)
        print('Площадь круга с радиусом', i, ':', '%.2f' % s)
