import math

while True:
    n = input('Введите коммадну <<Лого>> или <<Триго>> или <<Конец>>:')
    if n == 'Лого':
        f = input('Введите слово:')
        print(math.log(len(f)))
    if n == 'Триго':
        g = float(input('Введите градусы:'))
        r = math.radians(g)
        print(math.sin(r))
        print(math.cos(r))
        print(math.tan(r))
        print(math.atan(r))
    if n == 'Конец':
        break
