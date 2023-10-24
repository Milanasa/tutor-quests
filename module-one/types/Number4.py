#Опанасюк Н.Н.
try:
    inp = int(input("Введите число:"))
    outp = 0

    for i in str(inp):
        outp += int(i)
    print(outp)

except ValueError:
    print("!!!Неверный тип данных!!!")

input('Нажмите Enter, чтобы выйти...')