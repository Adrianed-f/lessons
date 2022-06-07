"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну.
Оформить в виде программы, которая считывает название города и выводит на печать страну.
"""


countries = {"Russia": ["Moscow", "Sochi", "Orel"],
             "Belarus": ["Minsk", "Mogilev", "Gomel"],
             "Ukraine": ["Kiev", "Odessa", "Lvov"]}


def find_country(city):
    for country, cities in countries.items():
        for item in cities:
            if item == city:
                return country


def main():
    print(find_country("Minsk"))
    print(find_country("Sochi"))
    print(find_country("Lvov"))


if __name__ == "__main__":
    main()
