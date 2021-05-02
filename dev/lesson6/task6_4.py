# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name=name
        self.is_police=is_police

    def go(self):
        return 'going'

    def stop(self):
        return 'stoping'

    def turn(self, direction):
        return f'turning {direction}'

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def show_speed(self):
        return self.speed

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Cpeed: {self.speed} --->>>  Alarm!!! <<<<---'
        else:
            return self.speed


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Cpeed: {self.speed} --->>>  Alarm!!! <<<<--- Piu, Piu, Piu'
        else:
            return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


mers = PoliceCar(300, 'white', 'GIBDD', True)

print(f'Auto {mers.get_name()} color: {mers.get_color()} speed: {mers.show_speed()} ')

vw = WorkCar(100, 'yellow', 'yellow Submarine', True)

print(f'Auto {vw.get_name()} color: {vw.get_color()} speed: {vw.show_speed()} ')

ford = SportCar(100, 'red', 'Red car', True)

print(f'Auto {ford.get_name()} color: {ford.get_color()} speed: {ford.show_speed()} ')


mazda = TownCar(70, 'red', 'Red mazda', True)

print(f'Auto {mazda.get_name()} color: {mazda.get_color()} speed: {mazda.show_speed()} ')