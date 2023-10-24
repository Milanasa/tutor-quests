#Опанасюк Н.Н.
try:
    a, b, c = map(float, input("Введите длину, ширину, высоту через пробел: ").replace(",", ".").split())
    print("Площадь стен: ", 2 * (a + b) * c)
except ValueError:
    print("!!!Неверный тип данных!!!")

input('Нажмите Enter, чтобы выйти...')