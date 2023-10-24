#Опанасюк Н.Н.
inp = str(input("Пишите тут: "))
inp = inp.strip()

while "  " in a:
    inp = inp.replace('  ', ' ')
print(inp)

input('Нажмите Enter, чтобы выйти...')