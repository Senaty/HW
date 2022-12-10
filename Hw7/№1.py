import random

n = int(input('Сколько четырёх значных чисел вы хотите записать?:'))
i = 0
with open('asd', 'w', encoding='utf-8') as output:
    while i <= n:
        a = random.randint(1000, 10000)
        i += 1
        print(a, file=output)
