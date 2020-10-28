#! /usr/bin/activate python
# -*- coding: utf-8 -*-

from math import sqrt
import math

print('Толпаров Натан ИУ5-51Б\n')

while True:
    try:
        a = float(input("A = "))
        break
    except ValueError:
        print('Неккоректно введенные данные.')

while True:
    try:
        b = float(input("B = "))
        break
    except ValueError:
        print('Неккоректно введенные данные.')

while True:
    try:
        c = float(input("C = "))
        break
    except ValueError:
        print('Неккоректно введенные данные.')

if a == 0 and b == 0 and c == 0:
    print('Корень уравнения любое число.')

elif c != 0 and b == 0 and a == 0:
    print('Нет решений.')

elif b != 0 and a == 0:
    x = -c / b
    if x < 0:
        print('Нет действительных корней.')
    elif x == 0:
        print('x = 0.00')
    else:
        print('x1 = %.2f' % (sqrt(x)) + ' x2 = %.2f' % (-sqrt(x)))

else:
    d = b ** 2 - 4 * a * c

    if d < 0:
        print('D < 0. Нет действительных корней.')

    else:
        t1, t2 = ((-b + sqrt(d)) / 2 * a), ((-b - sqrt(d)) / 2 * a)

        if t1 < 0 and t2 < 0:
            print('Нет действительных корней.')

        elif t1 > 0:
            print('x1 = %.2f' % (-1 * sqrt(t1)))
            print('x2 = %.2f' % (sqrt(t1)))
        elif t1 == 0:
            print('x = 0.00')
        if t2 > 0 and t1 != t2:
            print('x1 = %.2f' % (-1 * sqrt(t2)))
            print('x2 = %.2f' % (sqrt(t2)))
        elif t2 == 0 and t1 != t2:
            print('x = 0.00')

