a=int(input())
s=int(input())
if a>s:
    print(a,'-наибольшее число')
    print(s,'-наименьшее число')
elif a==s:
    print(a,'и',s,'-одинаковые числа')
else:
    print(a,'-наименьшее число')
    print(s,'-наибольшее число')