# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    __length: float
    __width: float
    __weight: float
    __thickness: float

    def __init__(self, length, width, weight=25, thickness=0.05) -> None:
        self.__length = length
        self.__width = width
        self.__weight = weight
        self.__thickness = thickness

    def get_mass_asp(self):
        self.mass =  self.__length * self.__width*self.__weight*self.__thickness
        return self.mass

road1 = Road(5000, 20)
road2 = Road(10000, 20)
print(road1.get_mass_asp())
print(road2.get_mass_asp())



