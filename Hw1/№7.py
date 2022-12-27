n = int(input('Введите число:'))
a = n // 100
b = n // 10 % 10
c = n % 10
if a > b and a > c:
    print('Наибольшее число:', a)
elif b > a and b > c:
    print('Наибольшее число:', b)
else:
    print('Наибольшее число:', c)
