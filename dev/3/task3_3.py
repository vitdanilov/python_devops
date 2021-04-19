# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    max1 = a + b
    v_max = '{}+{}'.format(a, b)
    if max1 < b + c:
        max1 = b + c
        v_max = '{}+{}'.format(b, c)
    if max1 < a + c:
        max1 = a + c
        v_max = '{}+{}'.format(a, c)
    return max1, v_max


def my_func2(a, b, c):
    m1, m2, m3 = a+b,b+c,a+c
    mdict = {m1:'{}+{}'.format(a,b),m2:'{}+{}'.format(b,c),m3:'{}+{}'.format(a,c)}
    return max(m1,m2,m3), mdict[max(m1,m2,m3)]


number_list = input("Введите 3 числа через пробел: ").split(" ")


if len(number_list) == 3:
    try:
        print("вариант 1")
        max1, v_max = my_func(int(number_list[0]), int(number_list[1]), int(number_list[2]))
        print("Максимальную сумму {} дало {}".format(max1, v_max))

        print("вариант 2")
        max2, v_max2 = my_func2(int(number_list[0]), int(number_list[1]), int(number_list[2]))
        print("Максимальную сумму {} дало {}".format(max2, v_max2))
    except ValueError as error:
        print("Ошибка ввода чисел")
else:
    print("Некорректные входные данные")


