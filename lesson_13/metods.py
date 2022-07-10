from faker import Faker
from sqlalchemy.orm import Session

from models import User, Profile, Address, Product, Purchase

fake = Faker()


def generate_user(session: Session) -> User:
    new_user = User(
        email=fake.email(), password=fake.word()
    )
    profile = Profile(
        user=new_user, phone=fake.phone_number(), age=fake.pyint(min_value=18, max_value=60)
    )
    address = Address(
        user=new_user, city=fake.city(), address=fake.address()
    )
    session.add_all([new_user, profile, address])
    session.commit()
    return new_user


def generate_purchase(session: Session):
    new_user = session.query(Session)
    new_product = Product(name=fake.company(), price=fake.pyfloat(min_value=20, max_value=100))
    purchase = Purchase(
        user=new_user, product=new_product, count=fake.pyint(min_value=1, max_value=5)
    )
    session.add_all([new_product, purchase])
    session.commit()


def add_product(session: Session):   # создание продукта
    new_product = Product(name=fake.company(), price=fake.pyfloat(min_value=20, max_value=100))
    session.add(new_product)
    session.commit()


def read_product(session: Session):   # вывод всех продуктов
    for products in session.query(Product).all():
        print(products.id, products.name, products.price, sep=" | ")


def read_users(session: Session):   # вывод всех пользователей
    for user in session.query(User).all():
        print(user.id, user.email, sep=" | ")


def refresh_product_by_id(session: Session, number: int, new_name: str, new_price: float):   # обновление продукта по id
    session.query(Product).filter_by(id=number).update({"name": new_name} and {"price": new_price})
    session.commit()


def delete_product(session: Session, number: int):   # удаление продукта из таблицы продуктов и таблицы покупок
    session.query(Product).filter_by(id=number).delete()
    session.query(Purchase).filter_by(product_id=number).delete()
    session.commit()


def buy_product(session: Session, count: int, email: str, product_name: str):   # покупка продукта юзеру(нужно выбрать)
    new_user = session.query(User).filter_by(email=email).first()
    new_product = session.query(Product).filter_by(name=product_name).first()
    purchase = Purchase(count=count, user=new_user, product=new_product)
    session.add(purchase)
    session.commit()


def view_purchases(session: Session, email: str):   # отображение покупок пользователя
    purchases = session.query(Purchase).join(User).join(Product).filter(
        User.email == email
    ).all()

    for purchase in purchases:
        print(purchase.product_id, purchase.product.name, purchase.product.price, purchase.count)


def filter_purchases_less(session: Session, limit_price: float):  # фильтрация по стоимости <
    purchases = session.query(Purchase).join(Product).filter(
        Product.price < limit_price
    ).all()
    for purchase in purchases:
        print(purchase.id, purchase.product_id, purchase.product.name)


def filter_purchases_more(session: Session, limit_price: float):  # фильтрация по стоимости >
    purchases = session.query(Purchase).join(Product).filter(
        Product.price > limit_price
    ).all()
    for purchase in purchases:
        print(purchase.id, purchase.product_id, purchase.product.name)


def view_users_who_buy_product(session: Session, product_name: str):   # пользователь по товару
    users = session.query(User).join(Purchase).join(Product).filter(
        Product.name == product_name
    ).all()
    for user in users:
        print(user.id, user.email, sep=" | ")
