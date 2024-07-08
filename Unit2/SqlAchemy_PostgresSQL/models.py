from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Genre(Base):
    __tablename__ = 'genres'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name_genre: Mapped[str]


class Author(Base):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name_author: Mapped[str]


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    title: Mapped[str]
    author: Mapped[int] = mapped_column(ForeignKey('authors.id', ondelete='CASCADE'))
    genre: Mapped[int] = mapped_column(ForeignKey('genres.id', ondelete='CASCADE'))
    price: Mapped[int]
    amount: Mapped[int]


class City(Base):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name_city: Mapped[str]
    days_delivery: Mapped[int]


class Client(Base):
    __tablename__ = 'clients'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name_client: Mapped[str]
    city_id: Mapped[int] = mapped_column(ForeignKey('cities.id', ondelete='CASCADE'))


class Buy(Base):
    __tablename__ = 'buy'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    buy_description: Mapped[str]
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.id', ondelete='CASCADE'))


class BuyBook(Base):
    __tablename__ = 'buy_books'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey('buy.id', ondelete='CASCADE'))
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id', ondelete='CASCADE'))
    amount: Mapped[int]


class Step(Base):
    __tablename__ = 'steps'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name_step: Mapped[str]


class BuyStep(Base):
    __tablename__ = 'buy_steps'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey('buy.id', ondelete='CASCADE'))
    step_id: Mapped[int] = mapped_column(ForeignKey('steps.id', ondelete='CASCADE'))
    date_step_beg: Mapped[datetime] = mapped_column(insert_default=func.now())
    date_step_end: Mapped[datetime] = mapped_column(insert_default=func.now())
