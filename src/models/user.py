# pyright: reportIncompatibleVariableOverride=false
# pyright: reportUnusedImport=false
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from src.shared.tools import get_random_str
from typing import TYPE_CHECKING

# for type check
if TYPE_CHECKING:
    from src.models.article import ArticleModel


class UserModel(SQLModel, table=True):
    __tablename__: str = "users"
    id: int = Field(primary_key=True)
    username: str = Field(default_factory=get_random_str, nullable=False, max_length=32)
    email: str = Field(..., nullable=False, max_length=128)
    telephone: str | None = Field(default=None, nullable=True, max_length=16)
    password: str = Field(..., nullable=False, max_length=128)
    avatar_url: str | None = Field(default=None, max_length=256)
    created_at: str = Field(default=datetime.now(), nullable=False)
    updated_at: datetime | None = Field(default=None, nullable=True)

    articles: list["ArticleModel"] = Relationship(back_populates="author")
