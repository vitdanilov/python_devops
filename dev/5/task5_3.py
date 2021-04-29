# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32


my_f = open("zzz5_3.txt", "r", encoding="utf-8")

count_row = 0
staffs = {}
for line in my_f:
    count_row += 1
    lst = line.replace('\n', '').split(" ")
    staffs[lst[0]] = float(lst[1])

my_f.close()
print("Первоначальный список: ")
print(staffs)

# staff_list = [x for x in staffs if (staffs[x] < 20000)]
# print("\nСледующие сотрудники имеют оклад менее 20 000:")
# print(staff_list)

staff_list = {x: staffs[x] for x in staffs if (staffs[x] < 20000)}
print("\nСледующие сотрудники имеют оклад менее 20 000:")

for key,value in staff_list.items():
    print(key, ':', value)

a = sum(staffs.values()) / len(staffs)
print("\nСредняя величина дохода всех сотрудников: {0:.2f}".format(a))

b = sum(staff_list.values())/len(staff_list)

print("\nСредняя величина дохода всех сотрудников получающих менее 20 000: {0:.2f}".format(b))
