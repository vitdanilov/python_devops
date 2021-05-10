# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
class MyOwnExc(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    goods = []

    @classmethod
    def reception(cls, obj):
        cls.goods.append(obj.my_unit)

    @classmethod
    def put_to_div(cls, obj, div):
        pass


class OfficeEquipment:
    model: str
    price: float

    # number_of_lists: int

    def __init__(self, model, price):
        self.model = model

        try:
            if isinstance(price, float):

                self.price = price

                self.my_unit = {
                    'Модель устройства': self.model,
                    'Цена за ед': self.price}
            else:
                self.my_unit = {}
                raise MyOwnExc("Вы ввели некорректную стоимость, словарь будем пустым")

        except MyOwnExc as e:
            print(e.txt)


class Printer(OfficeEquipment):
    def to_print(self):
        return f'модель {self.model} по цене {self.price}'


class Scaner(OfficeEquipment):
    def to_print(self):
        return f'модель {self.model} по цене {self.price}'

class Xerox(OfficeEquipment):
    def to_print(self):
        return f'модель {self.model} по цене {self.price}'

unit_1 = Printer('Printer hp', 2000.0)
print(unit_1.to_print())

unit_2 = Printer('Xerox', 1000.0)
print(unit_2.to_print())

unit_3 = Printer('Scaner', 1000.0)
print(unit_3.to_print())

Warehouse.reception(unit_1)
Warehouse.reception(unit_2)
Warehouse.reception(unit_3)

print(Warehouse.goods)