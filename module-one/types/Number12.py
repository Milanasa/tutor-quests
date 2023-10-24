#Опанасюк Н.Н.
sec = int(input("Введите количество секунд: "))
day_value = sec // 86400
sec_value = sec % (24 * 3600)
hour_value = sec_value // 3600
sec_value %= 3600
min_value = sec_value // 60
sec_value %= 60
print("Дни: " + str(day_value))
print("Часы: " + str(hour_value))
print("Минуты: " + str(min_value))
print("Секунды: " + str(sec_value))

input('Нажмите Enter, чтобы выйти...')