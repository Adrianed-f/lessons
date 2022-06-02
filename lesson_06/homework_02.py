"""
За каждой партой может сидеть не больше двух учеников.
Известно количество учащихся в каждом из трёх классов.
Cколько всего нужно закупить парт чтобы их хватило на всех учеников?
Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
"""


def number_of_desks(stud1, stud2, stud3):
    studs = [stud1, stud2, stud3]
    max_studs = studs[0]
    for item in studs:
        if item > max_studs:
            max_studs = item
    if max_studs % 2 != 0:
        desks = max_studs // 2 + 1
        return desks

    else:
        desks = max_studs // 2
        return desks


print("Количество парт:", number_of_desks(13, 16, 27))