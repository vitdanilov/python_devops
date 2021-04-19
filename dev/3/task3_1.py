# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def devision(val_1, val_2):
    try:
        res = val_1 / val_2
    except ZeroDivisionError:
        print("Деление на ноль запрещено")
        res = None

    return res


try:
    a = int(input("Введите число 1:"))
    b = int(input("Введите число 2:"))

    c = devision(a, b)

    if c is not None:
        print("{}/{} = {}".format(a, b, c))

except ValueError as error:
    print("Ошибка ввода числа")
