#Опанасюк Н.Н.
s = input("Введите последовательность скобок: ")
list = []
correct = True

for char in s:
    if char == '(':
        list.append('(')
    elif char == ')':
        if len(list) == 0:
            correct = False
            break
        elif list[-1] == '(':
            list.pop()

if (correct and len(list) == 0):
    print("Корректная последовательность")
else:
    print("Некорректная последовательность")

input('Нажмите Enter, чтобы выйти...')