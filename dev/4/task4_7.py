# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
import math
from itertools import count


def fact(n):
    #yield math.factorial(n)
    factorial = 1

    for x in count(1):
        if x > n:
            break

        factorial = factorial * x
        yield factorial

try:
    n = int(input("Введите целое число: "))
except ValueError as error:
    print("Ошибка ввода чисел")

i =0
for el in fact(n):
    i +=1
    print("{}!= {}".format(i, el))
