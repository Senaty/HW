n = set()
b = set()
for a in range(10, 23):
    n.add(a)
for s in range(30, 41):
    b.add(s)
print(n)
print(b)
d=int(input('какое число вы ищите?:'))
if d in (n or b):
    print('точка во множестве')
else:
    print('точка вне множества')