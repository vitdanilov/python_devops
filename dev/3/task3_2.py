# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def add_user(name, surname, year, city, email, phone):
    user = {'имя': name, 'фамилия': surname, 'год рождения': year, 'город проживания': city, 'email': email, 'телефон': phone}
    return user


name = input("Введите имя пользователя:")
surname = input("Введите фамилию пользователя:")
year = input("Введите год рождения пользователя:")
city = input("Введите город проживания пользователя:")
email = input("Введите email пользователя:")
phone = input("Введите phone пользователя:")

user = add_user(name=name, surname=surname, year=year, city=city, email=email, phone=phone)
print(user)
