import random

f = open('dsa.txt', 'w+')
n = ''
print('Стоп - остановка цикла')
while True:
    n = input('Вводите слова:')
    if n == 'Стоп':
        break
    else:
        with open('dsa.txt', 'a+', encoding='utf-8') as f:
            f.write(n+'\n')
with open('dsa.txt', 'r', encoding='utf-8') as f:
    g = f.read().splitlines()
print('I receive', random.choice(g))
print('You receive', random.choice(g))
