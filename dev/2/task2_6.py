# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
i = 0
lst = []
while True:
    i += 1
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара {}: ".format(name)))
    count = int(input("Введите колличество товара {}: ".format(name)))
    units = input("Введите единицы измерения товара {}: ".format(name))

    my_dict = {'название': name, 'цена': price, 'количество': count, 'ед': units}

    lst.append([i, my_dict])

    str = input("Для продолжения ввода нажмите Enter, для выхода 0: ")

    if str == "0":
        break;

print('Первоначальная структура')
print(lst)


lst_name = []
lst_price = []
lst_count = []
lst_units = []
for k in lst:
    lst_name.append(k[1]['название'])
    lst_price.append(k[1]['цена'])
    lst_count.append(k[1]['количество'])
    lst_units.append(k[1]['ед'])


my_dict2 = {'название': lst_name, 'цена': lst_price, 'количество': lst_count, 'ед': lst_units}

print('Итоговая структура')
print(my_dict2)