
N = int(input("Введите длину массива: "))
x = []
for i in range(N):
    print("Введите", i, "элементы массива: ")
    x.append(int(input()))
print("Максимальный элемент: " ,max(x))   
x.reverse()
print("Массив в обратном порядке:", x)
z = sum(x)/len(x)
x[0] = z
print("Замена нулевых элементов массива:", x)

    
