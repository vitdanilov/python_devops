# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, *args):
        self.lst = list(args)

    def __str__(self):
        lst2 = '\n'.join(map(str, self.lst))
        lst2 = lst2.replace(",","").replace("[","").replace("]","")

        return lst2

    def __add__(self, other):
        row =[]
        matrix_result = []
        for i in range(len(self.lst)):

            for j in range(len(self.lst[i])):
                row.append(self.lst[i][j] + other.lst[i][j])

            matrix_result.append(row)
            row = []

        return Matrix('\n'.join(map(str, matrix_result)))


matrix1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(matrix1)
print()

matrix2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(matrix2)
print()

print(matrix1+matrix2)