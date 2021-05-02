# 6. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки."

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title}. Pen'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title}. Pencil'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title}. Handle'

Stationery1 = Stationery("Вперёд")
print(Stationery1.draw())

pen1 = Pen("Жи ши")
print(pen1.draw())

Pencil1 = Pencil("пиши")
print(Pencil1.draw())

Handle1 = Handle("с буквой и")
print(Handle1.draw())