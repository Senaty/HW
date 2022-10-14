a=int(input())
s=int(input())
d=int(input())
a1=a//60
a2=a%60
s1=s//60
s2=s%60
d1=d//60
d2=d%60
h=10+a1+s1+d1
m=a2+s2+d2
while(m>60) or (h>24):
    if m >60:
        m=m-60
        h=h+1
    if h>24:
        h=h-24
print(h,m,sep=':')