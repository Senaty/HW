s = input()
while 1 == 1:
    if s == 'end':
        break
    if s.isdigit():
        print('Строка из цыфр')
    elif s.isalpha():
        print('Строка из букв')
    elif s.isalnum():
        print('Строка из цыфр и букв')
    else:
        continue
    s = input()
