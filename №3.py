import string

s = input()
while 1 == 1:
    if s == 'end':
        break
    elif s.isdigit():
        for i in s:
            print(10 * int(i))
    elif s.isalpha():
        for i in set(s):
            s.count(i)
            print(i, '=', s.count(i))
    else:
        for i in range(0, len(s)):
            if s[i] in string.punctuation:
                print(i, end=',')
    s = input()
