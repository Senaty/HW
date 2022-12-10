import math

with open('asd', 'w', encoding='utf-8') as output:
    a = float(input('Введите первое значение a:'))
    b = float(input('Введите второе значение b:'))
    h = float(input('Введите шаг смещения по оси x:'))
    m = int((max(a, b) - min(a, b)) // h)
    print(m)
    x = min(a, b)
    for i in range(0, m):
        print(((x * math.log(1 + (math.sin(x) / x))) / (x + math.sin(x)), ', при х =', x), file=output)
        x += h
