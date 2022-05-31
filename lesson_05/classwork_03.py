"""
Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент func_type.
В зависимости от func_type вернуть минимальное либо максимальное значение.
Написать программу в виде трех функций.
"""


def my_max(*args):
    max_item = args[0]
    for item in args:
        if item > max_item:
            max_item = item
    return max_item


def my_min(*args):
    min_item = args[0]
    for item in args:
        if item < min_item:
            min_item = item
    return min_item


def min_or_max(func_type, *args):

    if func_type == "min":
        result = my_min(*args)
    else:
        result = my_max(*args)
    return result


my_list = [1, 5, 16, 3, 66, -20, 5]

print(min_or_max("min", *my_list))

print(min_or_max("max", *my_list))
