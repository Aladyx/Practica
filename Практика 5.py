from itertools import count
n = "дом машина ель тюлень егерь егор"
count = 0
for i in n.split(" "):
    if i[0] == 'е':
        count +=1
print(count)