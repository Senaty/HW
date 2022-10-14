n=int(input("введите 3-х значное число:"))
a=n//100
s=n//10%10
d=n%10
if a>s and a>d: print(a)
elif s>a and s>d: print(s)
else: print(d)