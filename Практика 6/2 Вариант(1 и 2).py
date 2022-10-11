N = int(input("Введите длину массива: "))
x = []
y = []
p = []
for i in range(N):
    print("Введите", i, "элементы массива: ")
    x.append(int(input()))
print("Минимальный элемент массива:", min(x))
print("Индекс минимального элемента  массива: ", x.index(min(x)))
for i in x:
    if -i <= 0:
        y.append(i)
    else:
        p.append(i)
print("Массив положительных чисел: ", y)
print("Массив остальных чисел:", p)    
