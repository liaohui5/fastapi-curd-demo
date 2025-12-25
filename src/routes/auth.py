from src.shared.api_v1 import api_v1
from fastapi import Query


@api_v1.post("/register")
async def register():
    pass


@api_v1.post("/login")
async def login():
    pass


@api_v1.post("/refresh_access_token")
async def refresh_access_token(
    refresh_token: str = Query(..., description="refresh token"),
):
    pass
