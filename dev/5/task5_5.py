# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

out_f = open("out_file5_5.txt", "w")
my_list = [10, 25, 30, 45, 50]

count =0
for element in my_list:
    out_f.write(str(element))
    count += 1
    if count < len(my_list):
        out_f.write(' ')

out_f.close()

my_f = open("out_file5_5.txt", "r", encoding="utf-8")
staffs = {}

for line in my_f:
    my_list2 = line.split(" ")

my_f.close()

result=[]
result = [int(item) for item in my_list2]

print("Числа в файле: {}".format(result))
print("Сумма чисел в файле: {}".format(sum(result)))