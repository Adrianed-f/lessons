'''
Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.
'''

import random

r = random.randint(1, 10)
while r != 7:
    print(r)
    r = random.randint(1, 10)



