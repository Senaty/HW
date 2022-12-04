n = int(input())
s = ''
for i in range(n):
    i += 1
    i = input('Введите слово:')
    s += i[0]
print(s.upper())
