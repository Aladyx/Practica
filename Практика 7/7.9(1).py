def f(t):
    sum1 = 0
    while t > 0:
        sum1 += t % 10
        t = t // 10
    return sum1

x = int(input("Ваше число: "))
k = 0
while x > 0:
    x -= f(x)
    k += 1

print("Через ",k," действиий чсло будет равно 0" )    