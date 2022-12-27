k = 0
s = 0
for i in range(1, 5):
    a = int(input('Ваше число:'))
    if a % 2 == 1:
        k += 1
        s += a
print('Количество нечетных:', k)
print('Сумма нечетных', s)
