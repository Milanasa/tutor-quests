#Опанасюк Н.Н.
from statistics import mean

a = str(input('Пишите тут: ')).split()
c = []
i = 0
n = 0

for i in a:
    c.append(len(a[n]))
    n += 1
print(mean(c))

input('Нажмите Enter, чтобы выйти...')