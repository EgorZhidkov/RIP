import math
import cmath
from function_for_first_laba import is_digit
print('Жидков Егор Ильич, ИУ5-43Б')

a = 0
b = 0
c = 0
x1 = 0
x2 = 0
x3 = 0
x4 = 0 
print('Введите коэффициент A')
a = input()
while is_digit(a) != True:
    print("Коэффициент введен неправильно")
    a = input()
print('Введите коэффициент B')
b = input()
while is_digit(b) != True:
    print("Коэффициент введен неправильно")
    b = input()
print('Введите коэффициент C')
c = input()    
while is_digit(c) != True:
    print("Коэффициент введен неправильно")
    c = input()
a = float(a)
b = float(b)
c = float(c) 

D = (math.pow(b, 2) - (4 * a * c))
if D < 0:
    first_value_of_d = -100
    second_value_of_d = - 100
else:
    first_value_of_d = ((-b + math.sqrt(D)) / (2 * a))
    second_value_of_d = ((-b - math.sqrt(D)) / (2 * a))
check = False

if a == 0:
    if b == 0:
        if c == 0:
            print('x = 0')
        else:
            if (c / b) < 0:
                x1 = (math.sqrt(-(c/b)))
                x2 = -(math.sqrt(-(c/b)))
                print(x1 , x2)
            else:
                print('Нет решений')
    else:
        if c != 0:
            print('Нет решений')
        else:
            print('x любое')
else:
    if D < 0:
        print('Нет решений')
    else:
        if first_value_of_d > 0:
            x1 = math.sqrt(first_value_of_d)
            x2 = -(math.sqrt(first_value_of_d))
            print(x1, x2)
            check = True
        if second_value_of_d > 0:
            if check == True:
                x3 = math.sqrt(second_value_of_d)
                x4 = -(math.sqrt(second_value_of_d))
                print(x3, x4)
            else:
                x1 = math.sqrt(second_value_of_d)
                x2 = -(math.sqrt(second_value_of_d))
                print(x1, x2)


