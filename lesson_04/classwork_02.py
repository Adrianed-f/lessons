"""
Написать программу, которая выведет на экран все числа от 1 до 100 которые кратные n (n вводится с клавиатуры).
"""

number = int(input())

for item in range(1, 101):
    if item % number == 0:
        print(item)
