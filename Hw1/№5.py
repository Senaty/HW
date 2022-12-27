a = int(input('Первое число:'))
b = int(input('Второе число:'))
if a > b:
    print(a, '- наибольшее число')
    print(b, '- наименьшее число')
elif a < b:
    print(b, '- наибольшее число')
    print(a, '- наименьшее число')
else:
    print('Числа равны')
