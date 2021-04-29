# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.

import functools
import json

my_f = open("zzz5_7.txt", "r", encoding="utf-8")

firm = {}

for line in my_f:
    lst = line.replace('\n', '').split(" ")

    firm[lst[0]] = float(lst[2])-float(lst[3])

my_f.close()
average = 0
i=0
for key, value in firm.items():
    if value>0:
        i +=1
        average += value

average_profit = average/i

average_profit_dict = {"average_profit":average_profit}
lst2 = [firm, average_profit_dict]
print(lst2)

out_f = open("out_file5_7.txt", "w", encoding="utf-8")

json.dump(lst2, out_f, ensure_ascii=False)

out_f.close()