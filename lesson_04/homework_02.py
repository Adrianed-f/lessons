"""
Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран.
Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево
"""

pal = input("Введите строку: ")
if pal == pal[::-1]:
    print("Yes")
else:
    print("No")