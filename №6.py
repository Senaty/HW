import random

s = int(input())
n = []
for i in range(s):
    f = random.randint(0, 1)
    n.append(f)
a = n.count(0)
b = n.count(1)
ch = 0
c = [i for i, c in enumerate(n) if c == ch]
print(n)
print(a)
print(b)
print(c)
