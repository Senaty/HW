a = float(input('Расстояние, пройденое автомобилем:'))
b = float(input('за время:'))
c = a / b
if c < 30:
    print('Медленно')
elif c > 60:
    print('Быстро')
else:
    print("Средне")
