from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.models import Base

DATABASE_URL = "postgresql://bot_user:securepassword@localhost/bot_news"

# Асинхронное подключение к базе
database = Database(DATABASE_URL)

# Синхронное подключение для миграций и начальной настройки
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

