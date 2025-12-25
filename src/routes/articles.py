from src.shared.api_v1 import api_v1
from fastapi import Path
from src.validation.articles import CreateArticleSchema
from src.shared.response_fmt import ResponseFmt
from src.shared.curd import Curd
from src.models import ArticleModel
from src.shared.common import parse_pagination_query
from fastapi import Depends
from typing import Annotated


@api_v1.get("/articles")
async def list_articles(
    pagination: Annotated[dict[str, int], Depends(parse_pagination_query)],
):
    results = await Curd(ArticleModel).list_and_count(pagination)
    return ResponseFmt.success(results)


@api_v1.post("/articles")
async def create_article(article: ArticleModel):
    result = await Curd(ArticleModel).create(article)
    return ResponseFmt.success(result)


@api_v1.patch("/articles/{id}")
async def update_article(id: int = Path(..., description="文章 id")):
    pass


@api_v1.delete("/articles/{id}")
async def delete_article(id: int = Path(..., description="文章 id")):
    pass
