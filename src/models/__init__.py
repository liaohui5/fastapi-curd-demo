from sqlmodel import SQLModel, select, func, col
from src.models.user import UserModel
from src.models.article import ArticleModel
from src.config import Config
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession


# 注意驱动需要使用: aiosqlite 异步驱动
# 不能使用默认的 pysqlite, 因为它是同步的
# DB_URL = "sqlite+aiosqlite:///database.db"
DB_URL = Config.get_db_url()
engine = create_async_engine(DB_URL, echo=Config.is_debug_mode())


def create_async_session():
    return AsyncSession(engine)


__all__ = [
    "SQLModel",
    "UserModel",
    "ArticleModel",
    "create_async_session",
    "select",
    "func",
    "col",
]
