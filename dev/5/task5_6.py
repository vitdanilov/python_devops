# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import functools

my_f = open("zzz5_6.txt", "r", encoding="utf-8")

disciplines = {}
disciplines2 = {}
for line in my_f:
    lst = line.replace(':', '').replace('\n', '').replace('—', '0').replace('.', '').replace('(л)', '').replace('(пр)',
                                                                                                                '').replace(
        '(лаб)', '').split(" ")
    disciplines[lst[0]] = lst[1:]

    for key, value in disciplines.items():
        disciplines2[key] = functools.reduce(lambda a, b: int(a) + int(b), value)

print(disciplines)
print(disciplines2)

my_f.close()
