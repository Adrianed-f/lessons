'''
Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой строчный символ, из этих чисел составляется первый список.
Далее таким же образом вводятся второй и третий списки.
Вывести на экран список, элементы которого есть в первых двух списках, но отсутствуют в третьем.
'''
l1 = []

l2 = []

l3 = []

while True:
    c = input("Введите число: ")
    if c.isdigit():
        c = int(c)
        l1.append(c)
    else:
        break

print("Первый список:", l1)

while True:
    c = input("Введите число: ")
    if c.isdigit():
        c = int(c)
        l2.append(c)
    else:
        break

print("Второй список:", l2)

while True:
    c = input("Введите число: ")
    if c.isdigit():
        c = int(c)
        l3.append(c)
    else:
        break

print("Третий список:", l3)

l1.extend(l2)

for item in l1:
    for item2 in l3:
        if item == item2:
            l1.remove(item)

print("Финальный список:", l1)


