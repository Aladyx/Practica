n = 3
sum1 = 0
pl = 0
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
for i in range(len(a) - 1):
    for j in range(i + 1, len(a[i])):
        if a[i][j] > 0:
            sum1 += a[i][j]
            pl += 1
print('Cумму и число положительных элементов матрицы, \
    находящихся над главной диагональю: ',sum1, pl)
#Задание 2
for x in range(len(a)):
    idx = a[x].index(min(a[x]))
    a[x][idx], a[x][0] = a[x][0], a[x][idx]
    idx = a[x].index(max(a[x]))
    a[x][idx], a[x][-1] = a[x][-1], a[x][idx]
    
print('Измененый массив: ', a)
        

        
        
        
