n = 3
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    a.append(b)
#Вывод массива
for i in range(n):
    for j in range(n):
        print(a[i][j], end='')
    print()
#Задание 1
if sum(a[i]) == sum(a[j]):
    print('Матрица магическая')
else:
    print('Матрица не магическая')
#Задание 2       
for i in range(n):
    for j in range(n):
        x = a[i][0]
        a[i][0] = a[i][2]
        a[i][2] = x
for i in range(n):
    for j in range(n):
        print(a[i][j], end='')
    print()

    