def x(z, y, u):
  sum1 = sum(z)
  ar1 = sum(z)/len(z)
  sum2 = sum(y)
  ar2 = sum(y)/len(y)
  sum3 = sum(u)
  ar3 = sum(u)/len(u)
  Res1 = print("Сумма и среднеарефметическое значение 1-ого массива: ",sum1,",", ar1,";",
      "Сумма и среднеарефметическое значение 2-ого массива: ",sum2,",", ar2,";",
      "Сумма и среднеарефметическое значение 3-ого массива: ",sum3,",", ar3 )
  return Res1

N1 = int(input("Введите длину первого массива(Не больше 15): "))
if N1 >=15:
    print("Длинна массива больше 15")
    exit(0)
        
N2 = int(input("Введите длину второго массива(Не больше 15): "))
if N2 >=15:
    print("Длинна массива больше 15")
    exit(0)
    
N3 = int(input("Введите длину третьего массива(Не больше 15): "))
if N3 >=15:
    print("Длинна массива больше 15")
    exit(0)
    
z = []
y = []
u = []

for i in range(N1):
    print("Введите", i, "элементы 1-ого массива: ")
    z.append(int(input()))
    
for i in range(N2):
    print("Введите", i, "элементы 2-ого массива: ")
    y.append(int(input()))
    
for i in range(N3):
    print("Введите", i, "элементы 3-ого массива: ")
    u.append(int(input()))    

print(x(z, y, u))