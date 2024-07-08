from Unit2.SqlAchemy_PostgresSQL.database import engine
from Unit2.SqlAchemy_PostgresSQL.models import Base


def init_db():
    """Создание структуры БД"""

    Base.metadata.create_all(bind=engine)

