#Опанасюк Н.Н.
try:
    s = int(input("Введите число: "))
    print(s)
    print(float(s))
    print('"' + str(s) + '"')
    print(bool(s))
except ValueError:
    print("Неверный тип данных!")

input('Нажмите Enter, чтобы выйти...')