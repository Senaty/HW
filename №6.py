x, y = map(float, input("x, y = ").split())
if x * y > 0:
    if x > 0:
        print('Точка принадлежит первой четверти')
        s = input('Введи слово:')
        d = input('Введи другое слово:')
        if len(s) > len(d):
            print(d, '- Самая короткая строка')
        else:
            print(s, '- Самая короткая строка')
    else:
        print('Точка принадлежит третьей четверти')
        q = input('Введи слово:')
        print('x =',  (len(q)*x))
        print('y =',  (len(q)*y))
else:
    if x > 0:
        print('Точка принадлежит четвертой четверти')
        if abs(x) > abs(y):
            print('Координата x – наибольшая по модулю')
        elif abs(x) == abs(y):
            print('Координата равны наибольшая по модулю')
        else:
            print('Координата y – наибольшая по модулю')
    else:
        print('Точка принадлежит второй четверти')
        f = (2 * abs(x) - y) / y ** 2
        print(f)
