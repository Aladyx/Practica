a = int(input('Введите a: '))
b = int(input('Введите b: '))

if a < b:
    x = a + b
elif a > b:
    x = a - b
elif a == b:
    x = 1
print('X равен:', x)