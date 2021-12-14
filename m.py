import operator


def kalk(x, y, z):
    return z(x, y)


print(kalk(123, 2, operator.mul))


def square(x):
    a = (x, x ** 2, (x + x) * 2)
    return a


print(square(5))


def season(x):
    if 1 <= x <= 2 or x == 12:
        return 'winter'
    elif 3 <= x <= 5:
        return 'spring'
    elif 6 <= x <= 8:
        return 'summer'
    else:
        return 'autumn'


print(season(12))


def bank(a, year):
    return a + year * (a * 0.1)


print(bank(500, 2))


def is_prime(x):
    y = 2
    while y < x:
        if x % y == 0:
            return 'not'

        else:
            return 'prime'


print(is_prime(521))

from datetime import datetime, date, time


def date(day, mouth, year):
    return 1 <= day <= 30 and 1 <= day <= 31 and 1 <= mouth <= 12 and year == 2021


print(date(12, 12, 2021))


def XOR_cipher(string, key):
    return ' '.join(list(map(str, map(ord, string)))) ^ ' '.join(list(map(str, map(ord, key))))


#print(XOR_cipher(3, 5))
str1 = 'hello'
msg = ''
for i in str1:
    msg += (str(ord(i)))
print(msg)


def cipher(string, key):
    list1 = []
    for i in string:
        str((ord(i)))
        list1.append(str((ord(i)) ^ key))
    string1 = " ".join(list1)
    return list1


def un_cipher(a, key):
    for i in a:
        print(chr(int(i) ^ key), end='')


a = cipher(input('enter string: '), int(input('enter key un cipher: ')))
un_cipher(a, int(input('enter key: ')))



