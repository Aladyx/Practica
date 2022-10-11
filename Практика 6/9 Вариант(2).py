from random import *
a = [randint(1,10) for i in range(10)]
b = [randint(1,10) for i in range(10)]
print("Исходный массив А:", a)
print("Исходный массив B:", b)
y = a.copy()
a.clear()
a.extend(b)
b.clear()
b.extend(y)
print("Преобразованный массив А:" , a)
print("Преобразованный массив B:", b)
    
