from pydantic import BaseModel

class CreateArticleSchema(BaseModel):
    title: str
    content: str
    author_id: int




