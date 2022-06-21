"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
"""


import sqlite3


def create_products(name: str, price: int, amount: int, comment: str):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
           """
           INSERT INTO product (name, price, amount, comment)
           VALUES (?, ?, ?, ?);
           """,
           (name, price, amount, comment),
        )
    session.commit()


def read_products():
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM product
            """
        )
        session.commit()
    return cursor.fetchall()


def remove_product(id: int):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DELETE FROM product
            WHERE id = ?;
            """,
            (id,)
        )
        session.commit()
    return cursor.fetchall()


def refresh_product(id: int):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            UPDATE product
            SET price = price * 2 
            WHERE id = ?;
            """,
            (id, )
        )
        session.commit()
    return cursor.fetchall()


def main():
    circle = True
    while circle:
        print("1: создание\n2: чтение\n3: обновление(стоимости по id)\n4: удаление(по id)\n5: Выход")
        action = int(input())
        if action == 1:
            name = input("введите название:")
            price = int(input("введите стоимость:"))
            amount = int(input("введите количество:"))
            comment = input("введите комментарий:")
            create_products(name, price, amount, comment)
        elif action == 2:
            print(read_products())
        elif action == 3:
            number_refresh = int(input("введите id:"))
            refresh_product(number_refresh)
        elif action == 4:
            number_remove = int(input("введите id:"))
            remove_product(number_remove)
        elif action == 5:
            circle = False


if __name__ == "__main__":
    main()