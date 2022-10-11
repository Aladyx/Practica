m = int(input("Модуль: "))
N = int(input("Введите длину массива: "))
x = []
for i in range(N):
    print("Введите", i, "элемент массива: ")
    x.append(int(input()))
print("Изначальный массив: ", x)
for i in x:
    if abs(i) < m:
        print(i)

x.reverse()
print("Массив в обратном пордке: ", x)



    