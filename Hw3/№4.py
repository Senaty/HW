a = float(input('Введите два числа:\n'))
b = float(input())
while b != 0:
    print(a + b, a - b, a * b, a / b, sep='\n')
    a = float(input('Введите два числа:\n'))
    b = float(input())
print('На ноль делить нельзя!')
