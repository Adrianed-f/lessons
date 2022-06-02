"""
Доработать первое задание так, чтобы словарь читался из текстового CSV файла,
где на каждой строке пары слов вида: apple,яблоко.
"""


import  csv

d = {}
with open("dictionary.csv", "r") as file:
   reader = csv.reader(file)
   for row in reader:
       d[row[0]] = row[1]    #d = {row[0]: row[1] for row in reader}



def eng_to_rus(word):
    return d[word]


def rus_to_eng(word):
    for key, value in d.items():
        if value == word:
            return key


print(eng_to_rus("apple"))
print(rus_to_eng("Яблоко"))