from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Unit2.ParseWebSite.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=True)
session = sessionmaker(bind=engine)
