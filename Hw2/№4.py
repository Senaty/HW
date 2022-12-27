a = int(input("Ваше число:"))
b = a // 100
c = a // 10 % 10
d = a % 10


def mean3(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c


if max(b, c, d) - min(b, c, d) == mean3(b, c, d):
    print('Число', a, ' - "интересное"')
else:
    print('Число', a, ' - "не интересное"')
