"""
Создать python функцию, которая создает таблицу user, для примера использовать слайд №12.
Запустить функцию и проверить, что создался файл базы данных.
Cоздать функцию, которая позволяет добавлять данные в таблицу user. Добавить 5 различных записей.
"""


import sqlite3


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
           """
           INSERT INTO user (firstname, lastname, email, password, age)
           VALUES (?, ?, ?, ?, ?);
           """,
           (firstname, lastname, email, password, age),
        )
    session.commit()


if __name__ == "__main__":
    create_user("Alexander", "Chaika", "manti.by@gmail.com", "TestPass", 39)
    create_user("Alexander", "Chaiyka", "manti.by@gmail.com", "TestPass", 36)
    create_user("Alexander", "Chayka", "manti.by@gmail.com", "TestPasss", 37)
    create_user("Alexander", "Chayka", "manty.by@gmail.com", "TestPassssss", 37)