"""
Создать функцию для поиска всех пользователей с определенным именем.
Запустить функцию и найти хотя бы одного пользователя по имени.
"""
import sqlite3


def select_user(from_age: int, to_age: int) -> object:
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE age>= ? AND age<= ?;
            """,
            (from_age, to_age)
        )
        session.commit()
    return cursor.fetchone()


if __name__ == "__main__":
    print(select_user(10, 36))

