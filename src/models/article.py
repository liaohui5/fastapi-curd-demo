# pyright: reportIncompatibleVariableOverride=false
# pyright: reportUnusedImport=false
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from src.shared.tools import get_random_str
from src.models.user import UserModel

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from src.models.user import UserModel


class ArticleModel(SQLModel, table=True):
    __tablename__: str = "articles"
    id: int = Field(primary_key=True)
    author_id: int = Field(..., foreign_key="users.id")
    title: str = Field(default_factory=get_random_str, nullable=False, max_length=128)
    content: str = Field(..., nullable=False, max_length=128)
    like_count: int = Field(default=0, nullable=False)
    star_count: int = Field(default=0, nullable=False)
    share_count: int = Field(default=0, nullable=False)
    visit_count: int = Field(default=0, nullable=False)
    comment_count: int = Field(default=0, nullable=False)
    created_at: str = Field(default=datetime.now(), nullable=False)
    updated_at: datetime | None = Field(default=None, nullable=True)
    deleted_at: datetime | None = Field(default=None, nullable=True)

    author: UserModel | None = Relationship(back_populates="articles")
