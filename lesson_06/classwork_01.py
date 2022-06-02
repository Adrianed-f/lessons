"""
Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык.
Написать две функции, одна переводит слово с английского на русский, где слово - это входной параметр,
вторая функция - с русского на английский.
"""


d = {
    "apple" : "Яблоко",
    "banana" : "Банан",
    "red" : "Красный",
}


def eng_to_rus(word):
    return d[word]


def rus_to_eng(word):
    for key, value in d.items():
        if value == word:
            return key


print(eng_to_rus("apple"))
print(rus_to_eng("Яблоко"))