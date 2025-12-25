import sys
from pathlib import Path
import random
from datetime import datetime
from sqlmodel import create_engine, Session

sys.path.append(str(Path(__file__)))

from src.models import UserModel, ArticleModel


engine = create_engine("sqlite:///database.db", echo=True)


def create_session():
    return Session(bind=engine)


users_total = 5
articles_total = 50

# 123456 -> md5 -> bcrypt
password_hash_str = "$2a$12$IsDbbaxw.EnOzvkQgdDBjuGkDb3i3yTWS6MvoypV1PipHDMsaTYI6"


def create_users():
    user_list = []
    for i in range(1, users_total + 1):
        user = UserModel(
            id=i,
            username=f"user-{i}",
            email=f"user-{i}@example.com",
            password=password_hash_str,
        )
        user_list.append(user)
    return user_list


def create_articles():
    article_list = []
    for i in range(1, articles_total + 1):
        article_info = {
            "author_id": random.randint(1, users_total),
            "title": f"article{i}",
            "content": f"article{i} content",
        }
        article = ArticleModel(**article_info)
        article_list.append(article)
    return article_list


with create_session() as session:
    session.add_all(create_users())
    session.add_all(create_articles())
    session.commit()
