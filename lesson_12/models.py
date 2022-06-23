from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from decimal import Decimal

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    purchases = relationship("Purchase", back_populates="user")


class Purchase(Base):
    __tablename__ = "purchase"

    user_id = Column(ForeignKey("user.id"), primary_key=True)
    product_id = Column(ForeignKey("product.id"), primary_key=True)
    count = Column(Integer)

    user = relationship("User", back_populates="purchases")
    product = relationship("Product", back_populates="purchases")


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    purchases = relationship("Purchase", back_populates="product")


# class Profile(Base):
#     __tablename__ = "profile"
#     id = Column(Integer, primary_key=True)
#     phone = Column(String)
#     age = Column(Integer)
#
#     user_id = Column(Integer, ForeignKey("user.id"))
#     user = relationship("User", back_populates="profile")


# class Address(Base):
#     __tablename__ = "address"
#     id = Column(Integer, primary_key=True)
#     city = Column(String)
#     address = Column(Integer)
#
#     user_id = Column(Integer, ForeignKey("user.id"))
#     user = relationship("User", back_populates="addresses")
