# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

def sum_numbers(lst):
    sum_n = 0
    for num in lst:
        if num == 'z':
            return sum_n, 0
        sum_n += int(num)
    return sum_n, 1

sum_number = 0
literals_list = []
try:
    while True:
        print("Ведите несколько чисел, разделяя их пробелами, например: 1 2 3. Для выхода введите символ z")
        literals_list.extend(input("Ввод: ").split(" "))
        sum_number, res = sum_numbers(literals_list)

        if res == 0:
            literals_list.remove("z")
            print("Сумма чисел {} = {}".format(literals_list, sum_number))
            break
        else:
            print("Сумма чисел {} = {}".format(literals_list, sum_number))

except ValueError as error:
    print("Ошибка ввода чисел")

