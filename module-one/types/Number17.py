#Опанасюк Н.Н.
a = str(input("Введите Ф.И.О. тут: ")).split()
a1 = a[0]
a2 = a[1]
a3 = a[2]
space = ' '
point = '.'
print(a1 + space + a2[0] + point + a3[0] + point, end=space)
print(' ')

input('Нажмите Enter, чтобы выйти...')