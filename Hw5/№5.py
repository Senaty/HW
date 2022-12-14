N = int(input('Введите количество слов:'))
w = ""
for i in range(N):
    print(i + 1, '-е слово >>>', sep='')
    i = input()
    w += i[0]
print(w.upper())

###########################################################
w = input('Введите анализируемое слово >>>')
print("Общее кол-во символов в строке:", len(w))
print("Первый символ строки:", w[0])
print("Последний символ строки:", w[-1])
print("Строку в обратном порядке:", w[::-1])
print("Все символы с четными индексами:", w[::2])
print("Все символы с нечетными индексами:", w[1::2])

#######################################################
import string

w = input('Введите анализируемое слово >>>')
n = 0
if w.isalnum():
    for i in w:
        print(int(i) * 10, end=', ')
elif w.isalpha():
    for i in w:
        if i.upper() == 'Q':
            n += 1
    print(n)
else:
    for i in range(len(w)):
        if w[i] in string.punctuation:
            print(i, end=', ')

########################################################
while True:
    n = 0
    w = input("Задайте строку: >>>")
    if w.upper() == "STOP":
        break
    elif w.isalpha():
        print("Буквенная строка")
    elif w.isdigit():
        print("Цифровая строка")
    elif w.isascii():
        for i in w:
            if i in string.punctuation:
                n += 1
        if n == len(w):
            print('Знаковая строка')
        else:
            print('Смешаная строка')
