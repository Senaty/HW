s = str(input('Введите 3-х значное число:'))
a, b, c = int(s[0]), int(s[1]), int(s[2])
if a + b + c == 2 * max(a, b, c):
    print('Число',s,'- интересное')
else:
    print('Число',s,'- не интересное')