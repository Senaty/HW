a = 0
b = 0
c = 0
while (a == b) or (a == c) or (b == c):
    n = int(input('Введите число:'))
    a = str(n // 100)
    b = str(n // 10 % 10)
    c = str(n % 10)
    if (a != b) and (a != c) and (b != c):
        print(a + b + c, a + c + b, b + a + c, b + c + a, c + a + b, c + b + a, sep='\n')
    else:
        print("В числе есть одинаковые цифры, попробуйте снова!")
