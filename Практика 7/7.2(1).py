import math
def tr(a):
    tr = (math.sqrt(3)/4) * a ** 2
    S = tr * 6
    return S
a = int(input("Введите сторону а: "))

print(tr(a))