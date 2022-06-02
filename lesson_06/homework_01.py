"""
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное, в идеале не использовать библиотечные функции.
"""

def long_and_often(string):
    string = string.replace(",", "").replace(".", "")
    lst = string.split()
    max_len = len(lst[0])
    long_string = lst[0]
    for item in lst:
        if len(item) > max_len:
            max_len = len(item)
            long_string = item

    max_often = lst.count(lst[0])
    string_often = lst[0]
    for item in lst:
        if lst.count(item) > max_often:
            max_often = lst.count(item)
            string_often = lst[item]
    return long_string, string_often



text = "cat, apple, banana. cat, rabota. firefox."

print(long_and_often(text))

