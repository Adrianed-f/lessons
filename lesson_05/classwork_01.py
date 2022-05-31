"""
Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}".
Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.
"""


def format_str(name):
    print(f"Hello, {name}")


list_names = ["Nikita", "Zhenya", "Vlad", "Sasha", "Valera"]

for item in list_names:
    format_str(item)
