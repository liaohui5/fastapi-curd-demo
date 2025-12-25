from src.models import select, func, create_async_session, col
from datetime import datetime
from typing import Any


class Curd:
    def __init__(self, model):
        self.model = model
        self.session = create_async_session()

    def build_where(self, query, where: dict = {}):
        for field, value in where.items():
            query = query.where(col(field) == value)
        return query

    def build_query_where(self, where: dict = {}):
        query = select(self.model)
        if len(where) == 0:
            return query
        return self.build_where(query, where)

    async def count(self, where: dict = {}):
        async with self.session.begin():
            query = select(func.count(self.model.id))
            query = self.build_where(query, where)
            result = await self.session.exec(query)
            return result.one()

    async def list(self, pagination: dict[str, int], where: dict = {}):
        async with self.session.begin():
            offset = (pagination["page"] - 1) * pagination["limit"]
            limit = pagination["limit"]
            result = await self.session.exec(
                self.build_query_where(where).offset(offset=offset).limit(limit=limit)
            )
            return result.all()

    async def list_and_count(self, pagination: dict[str, int], where: dict = {}):
        count = await self.count(where)
        items = await self.list(pagination, where)
        return {
            "count": count,
            "items": items,
        }

    async def create(self, data: Any):
        async with self.session.begin():
            self.session.add(data)

    async def update(self, id: int, data: dict):
        async with self.session.begin():
            result = await self.session.exec(
                self.model.update().where(self.model.id == id).values(**data)
            )
        return result.rowcount

    async def delete(self, id: int):
        async with self.session.begin():
            data = {"deleted_at": datetime.now()}
            result = await self.session.exec(
                self.model.update().where(self.model.id == id).values(**data)
            )
            # await self.session.commit()
        return result.rowcount

    async def hard_delete(self, id: int):
        async with self.session.begin():
            result = await self.session.exec(
                self.model.delete().where(self.model.id == id)
            )
            # await self.session.commit()
        return result.rowcount

    async def detail(self, id: int):
        async with self.session.begin():
            result = await self.session.exec(
                self.model.select().where(self.model.id == id)
            )
        return result.one()
