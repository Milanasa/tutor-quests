#Опанасюк Н.Н.
try:
    digit = int(input("Введите число от 1 до 9:"))

    if digit<1 or digit>9:
        print("!!!Число не входит в дозволенный диапазон!!!")
    else:
        astr = str(digit)
        b = astr*2
        c = astr*3
        print(digit + int(b) + int(c))

except ValueError:
    print("!!!Неверный тип данных!!!")

input('Нажмите Enter, чтобы выйти...')