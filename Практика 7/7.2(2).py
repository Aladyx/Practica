from base64 import b16decode
from timeit import repeat


def x(a,b, a1, b1, a2, b2):
        S = a * b
        S1 = a1 * b1
        S2 = a2 * b2
        return S, S1, S2
a = int(input("Введите сторону а первого прямоугольника: "))
b = int(input("Введите сторону b первого прямоугольника: "))
a1 = int(input("Введите сторону а второго прямоугольника: "))
b1 = int(input("Введите сторону b второго прямоугольника: "))
a2 = int(input("Введите сторону а третьего прямоугольника: "))
b2 = int(input("Введите сторону b третьего прямоугольника: "))
print("Площадь трёх прямоугольников: ",x(a, b, a1, b1, a2, b2))
