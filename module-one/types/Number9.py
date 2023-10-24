#Опанасюк Н.Н.
a = str(input("Пишите тут: "))

while a:
    a1 = a[:1]
    print(a1[:1]*2, end='')
    a = a[1:]
print()

input('Нажмите Enter, чтобы выйти...')