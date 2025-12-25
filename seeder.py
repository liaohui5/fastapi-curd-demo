import sys
import random
from pathlib import Path
from dotenv import dotenv_values

sys.path.append(str(Path(__file__)))
from src.config import Config

Config.load_env(dotenv_values())

from src.models import UserModel, ArticleModel, create_async_session

users_total = 5
articles_total = 50

# 123456 -> md5 -> bcrypt
password_hash_str = "$2a$12$IsDbbaxw.EnOzvkQgdDBjuGkDb3i3yTWS6MvoypV1PipHDMsaTYI6"


def create_users():
    user_list = []
    for i in range(1, users_total + 1):
        user = UserModel(
            username=f"user-{i}",
            email=f"user-{i}@example.com",
            password=password_hash_str,
        )  # pyright: ignore [reportCallIssue]
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


session = create_async_session()


async def main():
    async with session:
        session.add_all(create_users())
        session.add_all(create_articles())
        await session.commit()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
