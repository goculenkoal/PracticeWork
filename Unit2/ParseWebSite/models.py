# Сохраняет полученные данные в таблицу «spimex_trading_results» со следующей структурой:
# g.      id
# h.      exchange_product_id
# i.       exchange_product_name
# j.       oil_id - exchange_product_id[:4]
# k.  	delivery_basis_id - exchange_product_id[4:7]
# l.       delivery_basis_name
# m.	delivery_type_id - exchange_product_id[-1]
# n.      volume
# o.      total
# p.      count
# q.      date
# r.       created_on
# s.      updated_on
from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class SpimexTradingResults(Base):
    __tablename__ = 'spimex_trading_results'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    exchange_product_id: Mapped[str]
    exchange_product_name: Mapped[str]
    oil_id: Mapped[str]
    delivery_basis_id: Mapped[str]
    delivery_basis_name: Mapped[str]
    delivery_type_id: Mapped[str]
    volume: Mapped[int]
    total: Mapped[int]
    count: Mapped[int]
    created_on: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc)
    )
    updated_on: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )
