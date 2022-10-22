S = (int(input('Расстояние в км:')))
t = (int(input('Время в часах:')))
U = S // t
if U < 30:
    print('Медленно')
elif 30 <= U <= 60:
    print('средне')
else:
    print('Быстро')
