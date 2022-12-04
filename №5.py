import random

s = int(input())
a = int(input())
b = int(input())
n = []
for i in range(s):
    f = random.randint(a, b)
    n.append(f)
print(n)
print(s)
print(max(n))
print(min(n))
n.sort()
print(n)
n.sort(reverse=True)
print(n)

