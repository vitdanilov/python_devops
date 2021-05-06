# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import abstractmethod, ABC


class AbstractWear(ABC):
    @abstractmethod
    def get_consumption(self):
        pass


    @abstractmethod
    def get_total_consumption(self):
        pass

class Wear(AbstractWear):
    name: str
    type: str
    consumption: float

    def __init__(self, name, type,  size=0, hight=0):
        self.name = name
        self.type = type
        self.size = size
        self.hight = hight

        if type=='пальто':
            self.consumption = self.size / 6.5 + 0.5
        else:
            self.consumption = self.hight * 2 + 0.3

    def get_consumption(self):
        return str(f'Расход ткани на {self.type}  {self.name} = {self.consumption:.2f}')

    @property
    def get_total_consumption(self):
        return self.consumption

coat = Wear(name="Кашемир", type="пальто", size=42)
costume = Wear(name="Шерстяной", type="костюм", hight=1.84)

print(coat.get_consumption())
print(costume.get_consumption())
total = coat.get_total_consumption+costume.get_total_consumption
print(str(f'Всего {total:.2f}'))




