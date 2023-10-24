#Опанасюк Н.Н.
s = input('Пишите тут: ').split()
maximum = count = 1

for i in range(len(s) - 1):
    if s[i][-1] == s[i + 1][0]:
        count += 1
    if s[i][-1] != s[i + 1][0] or i == len(s) - 2:
        maximum = max(count, maximum)
        count = 1

print(maximum if maximum > 1 else '0')

input('Нажмите Enter, чтобы выйти...')