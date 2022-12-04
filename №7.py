import random

s = int(input())
n = []
for i in range(s):
    f = random.randint(0, s)
    n.append(f)
print(n)
d = int(input('Какой символ убрать?:'))
while d in n:
    n.remove(d)
print(n)
