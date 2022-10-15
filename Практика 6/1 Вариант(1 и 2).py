
N = int(input("Введите длину массива: "))
x = []
for i in range(N):
    print("Введите", i, "элементы массива: ")
    x.append(int(input()))
print("Максимальный элемент: " ,max(x))   
x.reverse()
print("Массив в обратном порядке:", x)
z = sum(x)/len(x)
for i in range(N):
    if x[i] == 0:
        x[i] = z
print("Замена нулевого элемента массива:", x)

    
