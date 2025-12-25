from src.shared.api_v1 import api_v1
from fastapi import Path
from src.validation.articles import CreateArticleSchema
from src.shared.response_fmt import ResponseFmt


@api_v1.get("/articles")
async def list_articles():
    return ResponseFmt.success("todo it")


@api_v1.post("/articles")
async def create_article(create_article_form: CreateArticleSchema):
    pass


@api_v1.patch("/articles/{id}")
async def update_article(id: int = Path(..., description="文章 id")):
    pass


@api_v1.delete("/articles/{id}")
async def delete_article(id: int = Path(..., description="文章 id")):
    pass
