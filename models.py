import sqlalchemy as sql
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(length=50), unique=True)

    book = relationship("Book", back_populates="publisher")

    def __str__(self):
        return f"Publisher: id = {self.id}, name = {self.name}."


class Book(Base):
    __tablename__ = "book"

    id = sql.Column(sql.Integer, primary_key=True)
    title = sql.Column(sql.String(length=100), unique=True)
    id_publisher = sql.Column(sql.Integer, sql.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship("Publisher", back_populates="book")
    stock = relationship("Stock", back_populates="book")

    def __str__(self):
        return f"Book: id = {self.id}, title = {self.title}, id_publisher = {self.id_publisher}."


class Shop(Base):
    __tablename__ = "shop"

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(length=50), unique=True)

    stock = relationship("Stock", back_populates="shop")

    def __str__(self):
        return f"Shop: id = {self.id}, name = {self.name}."


class Stock(Base):
    __tablename__ = "stock"

    id = sql.Column(sql.Integer, primary_key=True)
    id_book = sql.Column(sql.Integer, sql.ForeignKey("book.id"), nullable=False)
    id_shop = sql.Column(sql.Integer, sql.ForeignKey("shop.id"), nullable=False)
    count = sql.Column(sql.Integer, nullable=False)

    book = relationship("Book", back_populates="stock")
    shop = relationship("Shop", back_populates="stock")
    sale = relationship("Sale", back_populates="stock")

    def __str__(self):
        return f"Stock: id = {self.id}, id_book = {self.id_book}, id_shop = {self.id_shop}, count = {self.count}."


class Sale(Base):
    __tablename__ = "sale"

    id = sql.Column(sql.Integer, primary_key=True)
    price = sql.Column(sql.String(length=10), nullable=False)
    date_sale = sql.Column(sql.DateTime, nullable=False)
    id_stock = sql.Column(sql.Integer, sql.ForeignKey("stock.id"), nullable=False)
    count = sql.Column(sql.Integer, nullable=False)

    stock = relationship("Stock", back_populates="sale")

    def __str__(self):
        return f"Sale: id = {self.id}, price = {self.price}, date_sale = {self.date_sale}, " \
               f"id_stock = {self.id_stock}, count = {self.count}."


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
