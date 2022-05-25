"""
Ввести с клавиатуры целое число n.
Получить сумму кубов всех целых чисел от 1 до n (включая n) используя цикл while.
"""

n = int(input())

i = int(1)

result = int(0)

while i <= n:
    result += i**3
    i += 1

print(result)
