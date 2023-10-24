#Опанасюк Н.Н.
inp = str(input("Пишите тут: ")).split()
inp.reverse()
print(max(inp, key=len))

input('Нажмите Enter, чтобы выйти...')