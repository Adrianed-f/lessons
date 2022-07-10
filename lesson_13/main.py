from faker import Faker
from sqlalchemy.orm import sessionmaker

from models import Base
from utils import setup_db_engine, create_database_if_not_exists
import metods

fake = Faker()

if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    circle = True
    while circle:
        print("1: создание продукта\n"
              "2: вывод продуктов\n"
              "3: вывод пользователей\n"
              "4: обновление продукта(название и стоимости по id)\n"
              "5: удаление продукта(по id)\n"
              "6: покупка продукта\n"
              "7: вывод всех покупок пользователя\n"
              "8: фильтрация продуктов меньшей стоимости\n"
              "9: фильтрация продуктов большей стоимости\n"
              "10: вывод пользователя по купленному товару\n"
              "11: Выход")
        action = int(input())
        if action == 1:
            metods.add_product(session=current_session)
        elif action == 2:
            metods.read_product(session=current_session)
        elif action == 3:
            metods.read_users(session=current_session)
        elif action == 4:
            number_refresh = int(input("введите id:"))
            new_price = float(input("введите новую стомость продукта:"))
            new_name = input("введите новое название продукта:")
            metods.refresh_product_by_id(session=current_session,
                                         number=number_refresh,
                                         new_name=new_name,
                                         new_price=new_price)
        elif action == 5:
            number_delete = int(input("введите id:"))
            metods.delete_product(session=current_session, number=number_delete)
        elif action == 6:
            metods.read_users(session=current_session)
            user = str(input("введите email пользователя для покупки продукта:"))
            metods.read_product(session=current_session)
            product = str(input("введите название продукта:"))
            count = int(input("введите количество:"))
            metods.buy_product(current_session, count=count, email=user, product_name=product)
        elif action == 7:
            metods.read_users(session=current_session)
            user = str(input("введите email пользователя:"))
            if metods.view_purchases(session=current_session, email=user) is None:
                print("У ЭТОГО ПОЛЬЗОВАТЕЛЯ НЕТ ПОКУПОК\nМОЖЕТЕ КУПИТЬ ЕМУ ЧТО НИБУДЬ)))")
        elif action == 8:
            limit_price = float(input("введите до какой стоимости отфильтровать покупки:"))
            metods.filter_purchases_less(session=current_session, limit_price=limit_price)
        elif action == 9:
            limit_price = float(input("введите от какой стоимости отфильтровать покупки:"))
            metods.filter_purchases_more(session=current_session, limit_price=limit_price)
        elif action == 10:
            metods.read_product(session=current_session)
            product = str(input("введите название продукта:"))
            if metods.view_users_who_buy_product(session=current_session, product_name=product) is None:
                print("НИКТО НЕ ПОКУПАЛ ЭТОТ ПРОДУКТ\nНО МОГУТ КУПИТЬ)))")
        elif action == 11:
            circle = False
