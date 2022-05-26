"""
Вывести в порядке возрастания все простые числа, расположенные между n и m (включая сами числа n и m), а также количество x этих чисел.
"""

n = int(input("Введите значение n: "))

m = int(input("Введите значение m: "))

s = []

x = int(0)


for item in range(n, m+1):

    for item2 in range(2, item):

        if item % item2 == 0:

            break

        elif item2 == item - 1:

            print(item)

            x += 1

print("количество простых чисел:", x)



