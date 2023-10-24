#Опанасюк Н.Н.
inp = str(input("Пишите тут: "))
inp = inp.strip()
while "  " in inp:
    inp = inp.replace('  ', ' ')
print(len(inp.split()))

input('Нажмите Enter, чтобы выйти...')