#Вариант 2.
#1. Дана целая квадратная матрица n-го порядка. Определить, является ли
#она магическим квадратом, т. е. такой матрицей, в которой суммы
#элементов во всех строках и столбцах одинаковы.
#2. Дана прямоугольная матрица A[N, N]. Переставить первый и
#последний столбцы местами и вывести на экран.




with open('M:\code\html\py\Буриков Никита Михайлович_УБ-23_vvod.txt', 'r', encoding='utf-8-sig') as file:
    line = file.readlines()
matrix = [element.replace("\n", "").split() for element in line]
file1 = open('M:\code\html\py\Буриков Никита Михайлович_УБ-23_vivod.txt', 'w')
n = len(matrix)
a = matrix
for i in range(n):
    for j in range(n):
        print(int(a[i][j]), end=" ")
    print()
#Задание 1
if a[i] == a[j]:
    print(file1.write('Матрица магическая\n\n'))
else:
    print(file1.write('Матрица не магическая\n\n'))
#Задание 2
for i in range(n):
    for j in range(n):
        x = a[i][0]
        a[i][0] = a[i][len(matrix[0]) - 1]
        a[i][len(matrix[0]) - 1] = x
print(file1.write('Изменённый массив:\n'))
#Запись массива в файл
for i in range(n):
    for j in range(n):
        print(file1.write(a[i][j] + ' '))
    print(file1.write('\n'))
file1.close()