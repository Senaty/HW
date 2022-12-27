a = int(input('Готовку:'))
b = int(input('Уборку:'))
c = int(input('Стирку:'))
a1 = a // 60
a2 = a % 60
b1 = b // 60
b2 = b % 60
c1 = c // 60
c2 = c % 60
h = 10 + a1 + b1 + c1
m = a2 + b2 + c2
d = 0
y = 0
while (m > 59) or (h > 24) or (d > 364):
    if m > 59:
        m = m - 60
        h = h + 1
    if h > 23:
        h = h - 24
        d += 1
    if d > 364:
        d = d - 365
        y += 1
if m == 0:
    print(h, m, sep=':', end='0')
elif m // 10 == 0:
    print(h, m, sep=':0')
else:
    print(h, m, sep=':')
print(d, 'Дней и', y, 'Лет')
