from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from Unit2.SqlAchemy_PostgresSQL.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=True)
Session = sessionmaker(bind=engine)
