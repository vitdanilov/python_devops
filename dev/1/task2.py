# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
time_sec = int(input("Введиет время в секундах: "))
time_hour = int(time_sec / 60 // 60)
if time_hour > 0:
    time_min = int((time_sec - time_hour * 60 * 60)/60)
else:
    time_min = time_sec // 60

time_sec = time_sec - time_hour*60*60 - time_min*60

time_str = 'Часов: {} Минут: {} Секунд: {}'.format(time_hour, time_min, time_sec)
print(time_str)
