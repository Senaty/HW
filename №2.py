n = [a for a in range(-4, 1)]
b = [s for s in range(3, 8)]
print(n)
print(b)
d = int(input('1 какое число вы ищите?:'))
f = int(input('2 какое число вы ищите?:'))
if (d in (n or b)) or (f in (n or b)):
    print('Yes')
else:
    print('No')
