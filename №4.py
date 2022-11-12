import random
import math

while True:
    a, b = int(input()), int(input())
    M = random.randint(a, b)
    if a == 0 or b == 0:
        print("Нули вводить низя >:(")
        n = input('Желаете продолжить? Y/N:')
        if n == 'N' or n == 'n':
            break
    elif a != 0 or b != 0:
        for i in range(1, M + 1):
            f = math.log10(i)
            print(f)
        n = input('Желаете продолжить? Y/N:')
        if n == 'N' or n == 'n':
            break
