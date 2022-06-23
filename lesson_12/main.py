from sqlalchemy.orm import sessionmaker, Session

from models import Base, User, Product, Purchase
from utils import setup_db_engine, create_database_if_not_exists


def create_user(session: Session, email: str, name: str, password: str, price: float, count: int) -> User:
    user = User(email=email, password=password)
    product = Product(name=name, price=price)
    purchase = Purchase(user=user, product=product, count=count)
    session.add_all([user, product, purchase])
    session.commit()

    return user


def add_product(session: Session, name: str, price: float) -> Product:
    product = Product(name=name, price=price)
    session.add(product)
    session.commit()

    return product


def read_products(session: Session):
    print(session.query(Product.id, Product.name, Product.price).all())


def refresh_product(session: Session, id: int, new_name: str, new_price: float):
    session.query(Product).filter_by(id=id).update({"name": new_name})
    session.query(Product).filter_by(id=id).update({"price": new_price})
    session.commit()


def delete_product(session: Session, id: int):
    session.query(Product).filter_by(id=id).delete()
    session.commit()


def buy_product(session: Session, count: int, id_user: int, id_product: int):
    new_user = session.query(User).filter_by(id=id_user).first()
    new_product = session.query(Product).filter_by(id=id_product).first()
    purchase = Purchase(count=count, user=new_user, product=new_product)
    session.add(purchase)
    session.commit()


def view_purchases(session: Session, user_id: int):
    purchases = session.query(Purchase.product_id).filter_by(user_id=user_id).all()
    for item in purchases:
        print("------------------------------:")
        print(session.query(Product.name, Product.price).filter_by(id=item[0]).all())
        print("------------------------------:")


def filter_purchases(session: Session, limit_price: float):  # фильтрация по стоимости <
    purchases = session.query(Purchase.product_id).all()
    for item in purchases:
        products = session.query(Product.price, Product.name).filter_by(id=item[0]).all()
        for item2 in products:
            if item2[0] < limit_price:
                print("НОМЕР ПОКУПКИ:", item[0])
                print("СТОИМОСТЬ ПРОДУКТА МЕНЬШЕ", limit_price)
                print(item2[0], item2[1])


# def update_or_create_address(session: Session, user: User, city: str, address: str) -> Address:
#     if len(user.addresses):
#         current_address = user.addresses[0]
#         current_address.city = city
#         current_address.address = address
#     else:
#         current_address = Address(user=user, city=city, address=address)
#
#     session.add(current_address)
#     session.commit()
#
#     return current_address


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    circle = True
    while circle:
        print("1: создание пользователя\n"
              "2: чтение продуктов\n"
              "3: обновление продукта(название и стоимости по id)\n"
              "4: удаление продукта(по id)\n"
              "5: покупка продукта\n"
              "6: вывод всех покупок пользователя\n"
              "7: фильтрация по произвольным параметрам(по стоимости: меньше чем...)\n"
              "8: Выход")
        action = int(input())
        if action == 1:
            email = input("введите email:")
            password = input("введите пароль:")
            name = input("введите название продукта:")
            price = float(input("введите стоимость:"))
            count = int(input("введите количество:"))
            create_user(session=current_session,
                        name=name,
                        password=password,
                        email=email,
                        price=price,
                        count=count)
        elif action == 2:
            print(read_products(session=current_session))
        elif action == 3:
            number_refresh = int(input("введите id:"))
            new_price = float(input("введите новую стомость продукта:"))
            new_name = input("введите новое название продукта:")
            refresh_product(session=current_session,
                            id=number_refresh,
                            new_name=new_name,
                            new_price=new_price)
        elif action == 4:
            number_delete = int(input("введите id:"))
            delete_product(session=current_session, id=number_delete)
        elif action == 5:
            print("id/email\n", current_session.query(User.id, User.email).all())
            user = int(input("введите id пользователя для покупки продукта:"))
            print("id/name/price\n", current_session.query(Product.id, Product.name, Product.price).all())
            product = int(input("введите id продукта:"))
            count = int(input("введите количество:"))
            buy_product(current_session, count=count, id_user=user, id_product=product)
        elif action == 6:
            print("id/email\n", current_session.query(User.id, User.email).all())
            user = int(input("введите id пользователя:"))
            view_purchases(session=current_session, user_id=user)
        elif action == 7:
            limit_price = float(input("введите до какой стомости отфильтровать покупки:"))
            filter_purchases(session=current_session, limit_price=limit_price)
        elif action == 8:
            circle = False

    #
    # new_user = current_session.query(User).filter_by(email="test@test.com").first()
    # update_or_create_address(
    #             session=current_session,
    #             user=new_user,
    #             city="bobor",
    #             address="address222")
    # new_user = create_user(
    #     session=current_session,
    #     email="Fabled@gamil.com",
    #     password="password",
    #     phone="phone",
    #     age=10,
    #     city="Minsk",
    #     address="address"
    # )
