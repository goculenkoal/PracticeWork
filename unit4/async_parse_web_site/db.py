from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=True)
session = sessionmaker(bind=engine)


# # DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#
# # engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=True)
# engine = create_async_engine(DATABASE_URL, pool_pre_ping=True, echo=True)
#
# async_session = async_sessionmaker(bind=engine)
# # session = sessionmaker(bind=engine)