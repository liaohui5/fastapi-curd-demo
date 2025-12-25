from sqlmodel import create_engine, Session, SQLModel
from src.models.user import UserModel
from src.config import Config


# 注意驱动需要使用: aiosqlite 异步驱动
# 不能使用默认的 pysqlite, 因为它是同步的
# DB_URL = "sqlite+aiosqlite:///database.db"
DB_URL = Config.get_db_url()
engine = create_engine(DB_URL, echo=True)


def create_session():
    return Session(engine)


__all__ = ["SQLModel", "UserModel", "engine", "create_session"]
