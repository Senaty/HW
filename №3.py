import random

N = int(input())
a = random.randint(0, 1000)
b = random.randint(0, 1000)
if max(a, b) < N < min(a, b):
    print('Lucky!')
elif max(a, b) > N > min(a, b):
    print('Lucky!')
else:
    print("Tru again!")
print(a)
print(b)
