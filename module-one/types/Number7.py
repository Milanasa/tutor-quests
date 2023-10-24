#Опанасюк Н.Н.
from fractions import Fraction

inp = str(input("Пишите тут: "))
length = len(inp)
fract = inp.count(" ")
print(Fraction(fract, length))

input('Нажмите Enter, чтобы выйти...')