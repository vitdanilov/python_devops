# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    count: int

    def __init__(self, count):
        self.count = count

    def __str__(self) -> str:
        return f'{self.count}'

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        i = self.count - other.count
        if i < 0:
            return "Ошибка вычитания"
        else:
            return Cell(i)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, cells_count):
        row = ''
        # print(f'self.count = {self.count}')
        for i in range(1, self.count+1):
            row += f"X"
            # print(row)
            # print(f'{i} % {cells_count} {i % cells_count}')
            if i % cells_count == 0:
                # print(row)
                row += "\n"
        return row

cell1 = Cell(10)
cell2 = Cell(5)

print(cell1)
print(cell2)
print(f'Складываем {cell1} + {cell2} = {cell1 + cell2}')
print(f"Вычитаем  {cell1} - {cell2} = {cell1 - cell2}")
print(f"Вычитаем  {cell2} - {cell1} = {cell2 - cell1}")
print(f"Умножаем  {cell2} * {cell1} = {cell2 * cell1}")
print(f"Делим  {cell1} / {cell2} = {cell1 / cell2}")
print(f"Делим  {cell2} / {cell1} = {cell2 / cell1}")

print("Организация ячеек по рядам")
print(cell1.make_order(5))
print(cell2.make_order(5))
cell3 = Cell(17)
print(cell3.make_order(4))