# 5. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

# Полагаю это косяк записи задания
# Предполагаю это часть предыдущего задания - поэтому здесь выполнен импорт и выпполнено по описаню

from lesson6 import task6_4

mers = task6_4.PoliceCar(300, 'white', 'GIBDD', True)

print(f'Auto {mers.get_name()} color: {mers.get_color()} speed: {mers.show_speed()} ')

vw = task6_4.WorkCar(100, 'yellow', 'yellow Submarine', True)

print(f'Auto {vw.get_name()} color: {vw.get_color()} speed: {vw.show_speed()} ')

ford = task6_4.SportCar(100, 'red', 'Red car', True)

print(f'Auto {ford.get_name()} color: {ford.get_color()} speed: {ford.show_speed()} ')


mazda = task6_4.TownCar(70, 'red', 'Red mazda', True)

print(f'Auto {mazda.get_name()} color: {mazda.get_color()} speed: {mazda.show_speed()} ')