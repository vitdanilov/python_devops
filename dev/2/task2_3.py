# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

month_1 = int(input("Введите месяц в виде целого числа от 1 до 12: "))
summer = [6, 7, 8]
winter = [12, 1, 2]
spring = [3, 4, 5]
fall = [9, 10, 11]

if month_1 in summer:
    print("Лето")
elif month_1 in winter:
    print("Зима")
elif month_1 in spring:
    print("Весна")
else:
    print("Осень")

# Вариант 2
seasons = {"summer": [6, 7, 8], "winter": [12, 1, 2], "spring": [3, 4, 5], "fall": [9, 10, 11]}


if month_1 in seasons["summer"]:
    print("Лето")
elif month_1 in seasons["winter"]:
    print("Зима")
elif month_1 in seasons["spring"]:
    print("Весна")
else:
    print("Осень")
