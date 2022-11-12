N, a, b = int(input()), int(input()), int(input())
for i in range(N, 0, -1):
    if i % 2 == 1:
        if i > max(a, b) or i < min(a, b):
            print(i)
