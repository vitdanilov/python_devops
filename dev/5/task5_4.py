# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

my_f = open("zzz5_4.txt", "r", encoding="utf-8")
out_f = open("out_file5_4.txt", "w", encoding="utf-8")

staffs = {}
for line in my_f:
    lst = line.replace("One","Один").replace("Two","Два").replace("Three","Три").replace("Four","Четыре").split(" ")
    #staffs[lst[0]] = float(lst[1])
    #lst = line.replace('\n', '').split(" ")
    out_f.writelines(lst)


my_f.close()
out_f.close()