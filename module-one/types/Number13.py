#Опанасюк Н.Н.
try:
    s = input("Пишите тут: ")

    length = len(s)
    digits = []
    i = 0

    while i < length:
        s_int = ''
        while i < length and '0' <= s[i] <= '9':
            s_int += s[i]
            i += 1
        i += 1
        if s_int != '':
            digits.append(int(s_int))
    print(digits)

except ValueError:
    print("!!!Неверный тип данных!!!")

input('Нажмите Enter, чтобы выйти...')