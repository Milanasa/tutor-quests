#Опанасюк Н.Н.
a = str(input("Пишите тут: "))

while a:
    a1 = a[:2]
    print(a1[::-1], end='')
    a = a[2:]
print()

input('Нажмите Enter, чтобы выйти...')