"""
Написать функцию, которая используя модуль requests скачивает файл сохраняет его на файловой системе,
функция имеет два параметра: ссылка на файл и имя на файловой системе.
В качестве примера ссылки на файл можно использовать лицензию из ГитХаба из вашего репозитория:
"""


import requests


def downoload(url, text):
    r = requests.get(url)
    f = open(text, "wb")
    f.write(r.content)
    f.close()


down = downoload("https://raw.githubusercontent.com/Adrianed-f/lessons/master/LICENSE", "/home/nikita/noname")
