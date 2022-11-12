import math

N = int(input())
for r in range(1, N+1):
    if r != 5:
        print('S', r, '=', f"{r ** 2 * math.pi:.3f}")
        print('L', r, '=', f"{r * 2 * math.pi:.3f}")
