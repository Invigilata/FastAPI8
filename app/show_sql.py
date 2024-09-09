from sqlalchemy.schema import CreateTable
from app.backend.db import engine, Base
from app.models.user import User
from app.models.task import Task

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Проверка SQL-запросов
print(CreateTable(User.__table__).compile(engine))
print(CreateTable(Task.__table__).compile(engine))
