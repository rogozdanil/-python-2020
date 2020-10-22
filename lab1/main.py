import math
import sys

print("Рогозин Данила ИУ5-51Б\n")
print("Нахождение корней квадратного уравнения")

if len(sys.argv) == 4:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except ValueError:
        print("Неправильные данные")
        sys.exit()

elif len(sys.argv) == 1:
    norm = True
    while norm:
        try:
            a = float(input("a = "))
            norm = False
        except ValueError:
            print("Неправильные данные")
            norm = True

    norm = True
    while norm:
        try:
            b = float(input("b = "))
            norm = False
        except ValueError:
            print("Неправильные данные")
            norm = True

    norm = True
    while norm:
        try:
            c = float(input("c = "))
            norm = False
        except ValueError:
            print("Неправильные данные")
            norm = True

else:
    print("Неправильное количество параметров командной строки")
    sys.exit()

print("a = {0}, b = {1}, c = {2}".format(a, b, c))

if a == 0 and b == 0 and c == 0:
    print("Корень уравнения: любое число")

elif a == 0 and b == 0 and c != 0:
    print("Нет решений")

elif a == 0 and b != 0:
    x = - c / b

    if x < 0:
        print("Уравнение не имеет действительных корней")
    elif x == 0:
        print("Корни уравнения: {0}".format(x))
    else:
        x1 = math.sqrt(x)
        x2 = -math.sqrt(x)
        print("Корни уравнения:")
        print("X1: {0}".format(x1))
        print("X@: {0}".format(x2))

else:
    d = b ** 2 - 4 * a * c

    if d < 0:
        print("Уравнение не имеет действительных корней")

    else:
        x1 = ((-1 * b) - math.sqrt(d)) / (2 * a)
        x2 = ((-1 * b) + math.sqrt(d)) / (2 * a)

        if x1 < 0 and x2 < 0:
            print("Уравнение не имеет действительных корней")

        else:
            print("Корни уравнения:")

            if x1 > 0:
                x1_1 = math.sqrt(x1)
                x1_2 = -1 * x1_1
                print("{0} {1}".format(x1_1, x1_2))

            elif x1 == 0:
                print(0)

            if 0 < x2 != x1:
                x2_1 = math.sqrt(x2)
                x2_2 = -1 * x2_1
                print("{0} {1}".format(x2_1, x2_2))

            elif x2 == 0 and x1 != x2:
                print(0)