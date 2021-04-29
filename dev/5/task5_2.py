# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_f = open("zzz5_2.txt", "r", encoding="utf-8")

count_row = 0
for line in my_f:
    print(line.replace('\n', ''))
    count_row += 1
    lst = line.split(" ")
    print("         Количество слов в строке: {}".format(len(lst)))

my_f.close()
print("Количество строк: {}".format(count_row))
