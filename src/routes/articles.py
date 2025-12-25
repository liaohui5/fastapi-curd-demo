from src.shared.api_v1 import api_v1
from fastapi import Path
from src.shared.response_fmt import ResponseFmt
from src.shared.curd import Curd
from src.models import ArticleModel
from src.shared.common import parse_pagination_query
from fastapi import Depends, Body
from typing import Annotated


@api_v1.get("/articles")
async def list_articles(
    pagination: Annotated[dict[str, int], Depends(parse_pagination_query)],
):
    results = await Curd(ArticleModel).list_and_count(
        pagination,
        {
            # only show articles that are not deleted
            ArticleModel.deleted_at: None
        },
    )
    return ResponseFmt.success(results)


@api_v1.post("/articles")
async def create_article(article: ArticleModel):
    result = await Curd(ArticleModel).create(article)
    return ResponseFmt.success(result)


@api_v1.patch("/articles/{id}")
async def update_article(
    id: int = Path(..., description="文章 id"), data: dict = Body()
):
    result = await Curd(ArticleModel).update(id, data)
    return ResponseFmt.success(result)


@api_v1.delete("/articles/{id}")
async def delete_article(id: int = Path(..., description="文章 id")):
    result = await Curd(ArticleModel).delete(id)
    return ResponseFmt.success(result)
