"""
Получить сумму кубов натуральных чисел от n до m используя цикл for, числа n и m вводятся с клавиатуры
"""

n = int(input("Введите значение n: "))

result = int(0)

m = int(input("Введите значение m: "))

for item in range(n, m+1):
    result += item**3
print(result)
